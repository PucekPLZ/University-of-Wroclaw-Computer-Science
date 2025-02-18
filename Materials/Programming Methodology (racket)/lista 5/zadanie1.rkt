#lang plait

; ('a 'b - > 'a )
(define (f1 a b)
  a)

; (('a 'b - > 'c ) ('a - > 'b ) 'a - > 'c )
(define (f2 f g x)
  (f x (g x)))

; ((( 'a - > 'a ) - > 'a ) - > 'a )
(define (f3 [f : (('a -> 'a) -> 'a)])
  (f (lambda (x) x)))

; (('a - > 'b ) ('a - > 'c ) - > ('a - > ('b * 'c ) ) )
(define (f4 [f : ('a -> 'b)] [g : ('a -> 'c)])
  (lambda (x) (pair (f x) (g x))))            ; pair : ('a 'b -> ('a * 'b))

; (('a - > ( Optionof ('a * 'b ) ) ) 'a - > ( Listof 'b ) )
(define (f5 f a)
  (if (some? (f a))                           ; some? : ((optionof 'a) -> bool)
      (cons (snd (some-v (f a)))              ; snd : (('a * 'b) -> 'b)  some-v : ((optionof 'a) -> 'a)
            (f5 f (fst (some-v (f a)))))      ; fst : (('a * 'b) -> 'a)
  '()))