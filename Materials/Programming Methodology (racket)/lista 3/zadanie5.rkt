#lang racket
(require rackunit)

(define (negatives n)
  (build-list n (lambda (x) (- (* (- 1) x) 1))))

(negatives 5)
(check-equal? (negatives 5) '(-1 -2 -3 -4 -5))

(define (reciprocals n)
  (build-list n (lambda (x) (/ 1 (+ x 1)))))

(reciprocals 5)
(check-equal? (reciprocals 5) '(1 1/2 1/3 1/4 1/5))

(define (evens n)
  (build-list n (lambda (x) (* x 2))))

(evens 5)
(check-equal? (evens 5) '(0 2 4 6 8))

(define (identityM n)
  (build-list n (lambda (x) (build-list n (lambda (y) (if (= y x) 1 0))))))

(identityM 4)
(check-equal? (identityM 4) '((1 0 0 0) (0 1 0 0) (0 0 1 0) (0 0 0 1)))
