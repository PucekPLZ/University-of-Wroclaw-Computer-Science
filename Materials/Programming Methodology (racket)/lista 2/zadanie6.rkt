#lang racket

(define (maximum xs)
  (define (it xs max)
    (cond [(null? xs)
                 max]
          [(> (car xs) max)
                 (it (cdr xs) (car xs))]
          [else (it (cdr xs) max)]))
  (if (null? xs)
      -inf.0
      (it xs (car xs))))

(define xs (list 1 5 0 2 1 0 1 8))

(maximum (list))
(maximum xs)