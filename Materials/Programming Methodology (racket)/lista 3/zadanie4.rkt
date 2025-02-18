#lang racket
(require rackunit)

(define (square x) (* x x))

(define (inc x) (+ x 1))

(define (my-compose f g)
  (lambda (x) (f (g x))))

((my-compose square inc) 5)
; ((my-compose square inc) 5) -> (square (inc 5)) -> (square (+ 5 1)) -> (square 6) -> (* 6 6) -> 36
(check-equal? ((my-compose square inc) 5) ((compose square inc) 5))

((my-compose inc square) 5)
; ((my-compose inc square) 5) -> (inc (square 5)) -> (inc (* 5 5)) -> (inc 25) -> (+ 25 1) -> 26
(check-equal? ((my-compose inc square) 5) ((compose inc square) 5))