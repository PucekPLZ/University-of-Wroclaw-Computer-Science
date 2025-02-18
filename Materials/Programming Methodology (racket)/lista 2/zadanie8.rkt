#lang racket

(define (sorted xs)
  (define (it i)
    (cond ((>= i (- (length xs) 1)) #t)
          ((> (list-ref xs i) (list-ref xs (+ i 1))) #f)
          (else (it (+ i 1)))))
  (it 0))

(sorted (list 1 2 3 4 5 6))
(sorted (list 1 6 3 4 5 6))