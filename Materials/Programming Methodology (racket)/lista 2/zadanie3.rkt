#lang racket

(define-struct matrix [a b c d] #:transparent)

(define m (matrix 1 2 3 4))

(define n (matrix 1 2 3 4))

(define (matrix-mult m n)
  (define matrix-mult-new (matrix
             (+ (* (matrix-a m) (matrix-a n)) (* (matrix-b m) (matrix-c n)))
             (+ (* (matrix-a m) (matrix-b n)) (* (matrix-b m) (matrix-d n)))
             (+ (* (matrix-c m) (matrix-a n)) (* (matrix-d m) (matrix-c n)))
             (+ (* (matrix-c m) (matrix-b n)) (* (matrix-d m) (matrix-d n)))))
  matrix-mult-new)

(matrix-mult m n)

(define matrix-id (matrix 1 0 0 1))

matrix-id

(define (matrix-expt m k)
  (cond [(= k 0)               
         matrix-id]
        [else                  
         (let ((mk-1 (matrix-expt m (- k 1))))
           (matrix-mult m mk-1))]))

(matrix-expt m 3)

(define f (matrix 1 1 1 0))

(define (fib-matrix k)
  (matrix-b (matrix-expt f k)))

(fib-matrix 15)