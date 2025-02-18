#lang racket

(require rackunit)

(define (elem x xs)
  (cond [(null? xs) #f] 
        [(equal? x (car xs)) #t] 
        [else (elem x (cdr xs))])) 


(define xs (list 1 2 3 4))

(elem 1 xs)
(elem 5 xs)