#lang racket
(require macro-debugger/stepper)

(define-syntax my-and
  (syntax-rules ()
    [(my-and) #t]
    [(my-and a b ...) (if a (my-and b ...) #f)] ))

(expand/step #'(my-and #t #f #t))

(define-syntax my-or
  (syntax-rules () 
    [(my-or) #f]
    [(my-or a b ...) (if a #t (my-or b ...))]))

(define-syntax my-let
  (syntax-rules ()
    [(my-let () a) a]
    [(my-let ([x1 a1] [x2 a2] ...) body)
     ((lambda (x1 x2 ...) body) a1 a2 ...)]))

(define-syntax my-let*
  (syntax-rules ()
    [(my-let* () a) a]
    [(my-let* ([x1 a1] [x2 a2] ...) body)
     ((lambda (x1) (my-let* ([x2 a2] ...) body)) a1)]))



; (let* ([a 5] [b (+ a 10)] [c 1]) (+ (+ c a) b))
; (my-let* ([a 5] [b (+ a 10)] [c 1]) (+ (+ c a) b))

#|
(module+ test
  (test (my-and) #t)
  (test (my-and #t) #t)
  (test (my-and #f) #f)
  (test (my-and #t #t #t) #t)
  (test (my-and #t #f #t) #f))

(module+ test
  (test (my-or) #f)
  (test (my-or #t) #t)
  (test (my-or #f) #f)
  (test (my-or #f #f #t) #t)
  (test (my-or #f #f #f) #f))

(module+ test
  (test (my-let () 42) 42)
  (test (my-let ([x 10] [y 20] [z 1]) (+ x (+ y z))) 31))

(module+ test
  (test (my-let* () 42) 42)
  (test (my-let* ([x 10] [y (+ x 20)]) (+ x y)) 40)
  (test (my-let* ([a 5] [b (+ a 10)] [c 1]) (+ (+ c a) b)) 21))
|#
