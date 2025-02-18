#lang racket

(define-struct matrix [a b c d] #:transparent)

(define (matrix-mult m n)
  (define matrix-mult-new (matrix
             (+ (* (matrix-a m) (matrix-a n)) (* (matrix-b m) (matrix-c n)))
             (+ (* (matrix-a m) (matrix-b n)) (* (matrix-b m) (matrix-d n)))
             (+ (* (matrix-c m) (matrix-a n)) (* (matrix-d m) (matrix-c n)))
             (+ (* (matrix-c m) (matrix-b n)) (* (matrix-d m) (matrix-d n)))))
  matrix-mult-new)

(define matrix-id (matrix 1 0 0 1))

(define (matrix-expt-fast m k)
  (cond [(= k 0)               
         (matrix-id)]
        [(= k 1)
         m]
        [(even? k)
         (let ((mk/2 (matrix-mult mk/2 mk/2))))
           (matrix-expt-fast m (- k 2))]
        [else
         (let ((mk-1 (matrix-expt-fast m (- k 1))))
           (matrix-mult m mk-1))]))

(define f (matrix 1 1 1 0))

(define (fib-fast k)
  (matrix-b (matrix-expt-fast f k)))

(fib-fast 15)

; log n