#lang racket

(define (suffixes xs)
  (if (null? xs)
      (list '())
      (cons xs (suffixes (cdr xs)))))

(define lst (list 1 2 3 4 5))

(suffixes lst)