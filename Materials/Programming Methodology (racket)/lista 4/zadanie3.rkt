#lang racket
(define-struct leaf () #:transparent)
(define-struct node (l elem r) #:transparent)

(define t
   (node
     (node (leaf) 2 (leaf))
     5
     (node (node (leaf) 6 (leaf))
            9
            (node (leaf) 9 (leaf)))))

; czy drzewo jest BST
(define (bst? t)
  (define (helper t mini maxi)
    (cond
      [(leaf? t) #t] 
      [(and (<= mini (node-elem t)) (< (node-elem t) maxi)) ; jeszcze jakas galaz do odwiedzenia 
       (and (helper (node-l t) mini (node-elem t)) (helper (node-r t) (node-elem t) maxi))] ; wywołanie od lewej (ustawiamy maxi jako rodzic) i od prawej (ustawiamy mini jako rodzic)
      [else #f])) ; w przeciwnym wypadku falsz
  (helper t -inf.0 +inf.0))

(bst? t)

; drzewo o tym samym kształcie co t, w którym etykietą danego węzła jest suma wartości węzłów na ścieżce od korzenia drzewa do tego węzła
(define (sum-paths t)
  (define (helper t sum)
    (cond
      [(leaf? t) (leaf)] ; koniec
      [(node? t)
           (node (helper (node-l t) (+ sum (node-elem t))) ; wywołanie od lewej 
                 (+ sum (node-elem t)) ; rodzic na sume
                 (helper (node-r t) (+ sum (node-elem t))))])) ; wywolanie od prawej
  (helper t 0))

(sum-paths t)