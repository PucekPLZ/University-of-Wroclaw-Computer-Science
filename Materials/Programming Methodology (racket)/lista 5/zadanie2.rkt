#lang plait

(define (apply f x)
  (f x))
; (apply : ('a -> 'b) 'a -> 'b)

(define (compose f g)
  (lambda (x)
    (f (g x))))
; (compose : (('a -> 'b) ('c -> 'a) -> ('c -> 'b)))

(define (flip f)
  (lambda (x y)
    (f y x)))
; (flip : (('a 'b -> 'c) -> ('b 'a -> 'c)))

(define (curry f)
  (lambda (x)
    (lambda (y)
      (f x y))))
; (curry : (('a 'b -> 'c) -> ('a -> ('b -> 'c))))