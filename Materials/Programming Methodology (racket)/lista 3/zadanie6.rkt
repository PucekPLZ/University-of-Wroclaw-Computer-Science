#lang racket

; zbior wartosci jako funkcja ktora zwraca prawde gdy wartosc jest w zbiorze, falsz gdy wartosci nie ma

(define (empty-set) (lambda (x) #f))

(define (singleton a) (lambda (x) (equal? a x)))

(define (in a s) (s a))

; x jest w s lub x jest w t - definicja sumy 
(define (union s t) (lambda (x) (or (s x) (t x))))

; x jest w s i jest w t - definicja przeciecia
(define (intersect s t) (lambda (x) (and (s x) (t x))))

