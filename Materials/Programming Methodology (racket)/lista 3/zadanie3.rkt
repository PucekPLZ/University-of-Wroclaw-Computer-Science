#lang racket
(require rackunit)


; Przyklad 1
((lambda (x y) (+ x (* x y))) 1 2)
; (+ 1 (* 1 2)) -> (+ 1 2) -> 3

; Przyklad 2
((lambda (x) x) (lambda (x) x))
; ((lambda (x) x) (lambda (x) x)) -> (lambda (x) x)
; (lambda (x) x) identity function - zwraca swoj argument niezmieniony

(define f (lambda (x) x))
; (f f) -> ((lambda (x) x) f) -> f -> (lambda (x) x)
(check-equal? f (f f))

; Przyklad 3
((lambda (x) (x x)) (lambda (x) x))
; ((lambda (x) (x x)) (lambda (x) x)) -> ((lambda (x) x) (lambda (x) x)) -> (lambda (x) x)
; funkcja (lambda (x) (x x)) stosuje swoj argument, który jest funkcja, do samego siebie 

; Przyklad 4
; ((lambda (x) (x x)) (lambda (x) (x x)))
; ((lambda (x) (x x)) (lambda (x) (x x))) -> ((lambda (x) (x x)) (lambda (x) (x x))) -> ((lambda (x) (x x)) (lambda (x) (x x))) -> ...
; infinite loop