#lang racket

(define (fib n)
  (cond [(= n 0) 0]
        [(= n 1) 1]
        [else (+ (fib (- n 1)) (fib (- n 2)))]))

(fib 17)

(define (fib-iter n)
  (define (it n acc)
    (cond [(= n 0) (- acc 1)]
          [(= n 1) acc]
          [else (+ (it (- n 1) acc) (it (- n 2) acc))]))
  (it n 1))

(fib-iter 17)


(time (fib 30))
(time (fib-iter 30))