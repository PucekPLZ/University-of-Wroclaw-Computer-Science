#lang racket

(require rackunit)

(define (my-foldl f x xs)
  (define (it xs acc)
    (if (null? xs)
        acc
        (it (cdr xs) (f (car xs) acc))))
  (it xs x))

(define (product xs)
  (my-foldl * 1 xs))

(define xs (list 2 3 4))
(product xs)
(product '())

(apply * '())

(check-equal? (product xs) (foldl * 1 xs))
(check-equal? (product xs) (apply * xs))