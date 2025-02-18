#lang racket

(define (minimum xs)
  (define (it xs min)
    (cond [(null? xs)
                 min]
          [(< (car xs) min)
                 (it (cdr xs) (car xs))]
          [else (it (cdr xs) min)]))
  (if (null? xs)
      -inf.0
      (it xs (car xs))))

(define (select xs)
  (cons (minimum xs) (remove (minimum xs) xs)))

(define lst (list 1 2 34 -2 67 28 -2 384 1 1 92))

(define (selection-sort xs)
  (if (null? xs)
      '()
      (cons (car (select xs)) (selection-sort (cdr (select xs))))))

(selection-sort lst)  