#lang plait

(module+ test
  (print-only-errors #t))

;; abstract syntax -------------------------------

(define-type Exp
  (numE [n : Number])
  (varE [x : Symbol])
  (opE  [op : (Number Number -> Number)] [l : Exp] [r : Exp])
  (defE [args : (Listof Exp)] [e : Exp])
  (funE [name : Exp] [args : (Listof Exp)] [body : Exp])
  (ifzE [e0 : Exp] [e1 : Exp] [e2 : Exp])
  (letE [x : Exp] [e1 : Exp] [e2 : Exp])
  (appE [f : Exp] [args : (Listof Exp)]))

;; parse -----------------------------------------

(define (fifth xs)
  (list-ref xs 4))

(define (sixth xs)
  (list-ref xs 5))

(define (parse [s : S-Exp]) : Exp
  (cond
    [(s-exp-match? `{define {ANY ...} for ANY} s)
      (defE (map parse (s-exp->list (second (s-exp->list s))))
            (parse (fourth (s-exp->list s))))]
    [(s-exp-match? `{fun SYMBOL {ANY ...} = ANY} s)
     (funE (parse (second (s-exp->list s)))
           (map parse (s-exp->list (third (s-exp->list s))))
           (parse (fifth (s-exp->list s))))]
    [(s-exp-match? `{let SYMBOL be ANY in ANY} s)
     (letE (parse (second (s-exp->list s)))
           (parse (fourth (s-exp->list s)))
           (parse (sixth (s-exp->list s))))]
    [(s-exp-match? `{ifz ANY then ANY else ANY} s)
     (ifzE (parse (second (s-exp->list s)))
           (parse (fourth (s-exp->list s)))
           (parse (sixth (s-exp->list s))))]
    [(s-exp-match? `{SYMBOL {ANY ...}} s)
     (appE (parse (first (s-exp->list s)))
           (map parse (s-exp->list (second (s-exp->list s)))))]
    [(s-exp-match? `NUMBER s)
     (numE (s-exp->number s))]
    [(s-exp-match? `SYMBOL s)
     (varE (s-exp->symbol s))]
    [(s-exp-match? `{ANY SYMBOL ANY} s)
     (opE (parse-op (s-exp->symbol (second (s-exp->list s))))
          (parse (first (s-exp->list s)))
          (parse (third (s-exp->list s))))]
    [else (error 'parse "invalid input")]))

(define (<= [x : Number] [y : Number]) : Number
  (if (or (< x y) (= x y))
      0
      23))

(define (parse-op [op : Symbol]) : (Number Number -> Number)
  (cond
    [(eq? op '+)   +]
    [(eq? op '-)   -]
    [(eq? op '*)   *]
    [(eq? op '<=) <=]
    [else (error 'parse "unknown operator")]))

;; eval ------------------------------------------

;; Values

(define-type-alias Value Number)

;; environments

(define-type Storable
  (valS [v : 'a]))

(define-type Binding
  (bind [name : Symbol]
        [ref : (Boxof Storable)]))

(define-type-alias Env (Listof Binding))

(define mt-env empty)

(define (extend-env [env : Env] [x : Symbol] [v : 'a]) : Env
  (cons (bind x (box (valS v))) env))

(define (extend-env-vars [env : Env] [vars : (Listof Exp)] [args : (Listof Value)]) : Env
  (type-case (Listof Exp) vars
    [(cons fun funs)
     (type-case Exp fun
       [(varE x)
        (if (find env x)
            (error 'eval "symbol already used")
            (extend-env-vars (extend-env env x (first args)) funs (rest args)))]
       [else (error 'eval "bad type")])]
    [empty env]))

(define (extend-env-func [env : Env] [funs : (Listof Exp)]) : Env
  (type-case (Listof Exp) funs
    [(cons fun funs)
     (type-case Exp fun
       [(funE name args body)
        (type-case Exp name
          [(varE x)
           (if (find env x)
               (error 'define "symbol already used")
               (extend-env-func (extend-env env x fun) funs))]
          [else (error 'define "bad type")])]
       [else (error 'define "not a function")])]
    [empty env]))

(define (find-var [env : Env] [x : Symbol]) : (Boxof Storable)
  (type-case (Listof Binding) env
    [empty (error 'lookup "unbound expression")]
    [(cons b rst-env)
     (cond
       [(eq? x (bind-name b))
        (bind-ref b)]
       [else
        (find-var rst-env x)])]))

(define (find [env : Env] [f : Symbol]) : Boolean 
  (type-case (Listof Binding) env
    [(cons x xs)
     (if (eq? (bind-name x) f)
         #t
         (find xs f))]
    [empty #f]))

(define (lookup-env [x : Symbol] [env : Env]) : 'a
  (type-case Storable (unbox (find-var env x))
    [(valS v) v]))

;; evaluation function

(define (eval [e : Exp] [env-var : Env] [env-fun : Env]) : Value
  (type-case Exp e
    [(defE args e)
     (eval e env-var (extend-env-func env-fun args))]
    [(numE n) n]
    [(varE x)
     (lookup-env x env-var)]
    [(ifzE e0 e1 e2)
     (if (= (eval e0 env-var env-fun) 0)
         (eval e1 env-var env-fun)
         (eval e2 env-var env-fun))]
    [(letE x e1 e2)
     (type-case Exp x
       [(varE x)
        (let ([v1 (eval e1 env-var env-fun)])
          (eval e2 (extend-env env-var x v1) env-fun))]
       [else (error 'eval "bad type")])]
    [(opE op l r)
     (op (eval l env-var env-fun) (eval r env-var env-fun))]
    [(appE f args)
     (type-case Exp f
       [(varE x)
        (apply x args env-var env-fun)]
       [else (error 'eval "bad type")])]
    [(funE name args body)
     (error 'eval "function can not be evaluated")]))

(define (apply [f : Symbol] [args : (Listof Exp)] [env-var : Env] [env-fun : Env]) : Value
  (type-case Exp (lookup-env f env-fun)
    [(funE name vars body)
     (if (= (length vars) (length args))
         (let ([evaluated-args (map (lambda (arg) (eval arg env-var env-fun)) args)])
           (eval body (extend-env-vars mt-env vars evaluated-args) env-fun))
         (error 'apply "wrong number of argument"))]
    [else (error 'apply "not a function")]))

(define (run [program : S-Exp]) : Value
  (eval (parse program) mt-env mt-env))

;; testy

#;(module+ test
  (test (parse `7)
        (numE 7))
  (test (parse `x)
        (varE 'x))
  (test (parse `{1 + 2})
        (opE + (numE 1) (numE 2)))
  (test (parse `{-34 - -5})
        (opE - (numE -34) (numE -5)))
  (test (parse `{3 * 3})
        (opE * (numE 3) (numE 3)))
  (test (parse `{-67 <= -99})
        (opE <= (numE -67) (numE -99)))
  (test/exn (parse `{{* 4 2}})
            "parse: invalid input")
  (test/exn (parse `{+ 1})
            "parse: invalid input")
  (test/exn (parse `{1 % 2})
            "parse: unknown operator")
  (test (parse `{ifz {8 - 5} then 3 else 14})
        (ifzE (opE - (numE 8) (numE 5)) (numE 3) (numE 14)))
  (test (parse `{let x be {2 - 3} in {42 * {x * x}}})
        (letE (varE 'x) (opE - (numE 2) (numE 3))
              (opE * (numE 42) (opE * (varE 'x) (varE 'x)))))
  (test (parse `{f {x1 x2 x3}})
        (appE (varE 'f) (list (varE 'x1) (varE 'x2) (varE 'x3))))
  (test (parse `{f {}})
        (appE (varE 'f) (list)))
  (test (parse `{fun f {x1 x2 x3} = {x1 + (x2 - x3)}})
        (funE (varE 'f)
              (list (varE 'x1) (varE 'x2) (varE 'x3))
              (opE + (varE 'x1) (opE - (varE 'x2) (varE 'x3)))))
  (test (parse `{define {{fun f {x1 x2} = {x1 * x2}} {fun g {x1} = {x1 * x1}}}
                  for {{f {x1 x2}} + {g {x1}}}})
        (defE (list (funE (varE 'f)
                          (list (varE 'x1) (varE 'x2))
                          (opE * (varE 'x1) (varE 'x2)))
                    (funE (varE 'g)
                          (list (varE 'x1))
                          (opE * (varE 'x1) (varE 'x1))))
          (opE + (appE (varE 'f) (list (varE 'x1) (varE' x2)))
               (appE (varE 'g) (list (varE 'x1)))))))

#;(module+ test
  (test (run `{5 - 3})
        2)
  (test (run `{4 * 2})
        8)
  (test (run `{7 + 6})
        13)
  (test (run `{7 <= 14})
        0)
  (test (run `{10 <= 5})
        23)
  (test (run `{{5 - 2} * {3 + {4 * 2}}})
        33)
  (test (run `{ifz {2 <= 1} then {3 * 3} else 64})
        64)
  (test (run `{let y be 2 in {y + 2}})
        4)
  (test (run `{let z be 3 in {z + {let w be 2 in {z * w}}}})
        9)
  (test (run `{let x be 2 in {x + {let x be {x * 2} in {x - 1}}}})
        5))

#;(module+ test
  (test (run `{define
                {[fun fact (n) = {ifz n then 1 else {n * {fact ({n - 1})}}}]}
                for {fact (5)}})
        120)
  (test (run `{define
                {[fun even (n) = {ifz n then 0 else {odd ({n - 1})}}]
                 [fun odd (n) = {ifz n then 42 else {even ({n - 1})}}]}
                for {even (1024)}})
        0)
  (test (run `{define
                {[fun gcd (m n) = {ifz n then m else
                                       {ifz {m <= n}
                                            then {gcd (m {n - m})}
                                            else {gcd ({m - n} n)}}}]}
                for {gcd (81 63)}})
        9))

#;(module+ test
  (test/exn (run `{define
                    {[fun sum (x y x) = {{x + y} + x}]}
                    for {sum (81 63 9)}})
                    "eval: symbol already used")
  (test/exn (run `{define 
                   {[fun product (x y z) = {{x * y} * z}]} 
                   for {product (10 20)}})
            "apply: wrong number of argument")

  (test/exn (run `{define 
                   {[fun div (x y) = {x / y}]} 
                   for {div (10 0)}})
            "parse: unknown operator") 

  (test/exn (run `{define 
                   {[fun sum (x y z) = {{x + y} + z}]}
                   for {sum (5 5 a)}})
            "lookup: unbound expression")

  (test/exn (run `{define 
                   {[fun square (x) = {x * x}]} 
                   for {circle (10)}})
            "lookup: unbound expression")

  (test/exn (run `{define 
                   {[fun mult (x y) = {{x * y} * y}]} 
                   for {mult (5)}})
            "apply: wrong number of argument")
            
  (test/exn (run `{define 
                   {[fun diff (x y) = {x - y}]} 
                   for {diff (5 "6")}}) 
            "parse: invalid input")
            
  (test/exn (run `{define 
                   {[fun increment (x) = {x + 1}]} 
                   for {increment (x)}})
            "lookup: unbound expression")
  (test/exn (run `{fun error (x) = {{x * x} + 1}})
            "eval: function can not be evaluated")
  (test/exn (run `{define
                    {let sub be 1 in {sub + 1}}
                    for {sub (81 63)}})
            "define: not a function"))