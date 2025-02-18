#lang racket
(require rackunit)

(define (sum-square x y)
  (+ (* x x) (* y y)))

(define (square a b c)
  (cond [(and (> a b) (> c b)) (sum-square a c)]
        [(and (> a c) (> b c)) (sum-square a b)]
        [else (sum-square b c)]))

(square 5 7 3)


(check-equal? (square 5 7 3) (sum-square 5 7))

(square 10 1 25)

(check-equal? (square 10 1 25) (sum-square 10 25))

(check-equal? (square 10 1 25) (sum-square 2 10))