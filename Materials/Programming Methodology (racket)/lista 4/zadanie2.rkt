#lang racket
(define-struct leaf () #:transparent)
(define-struct node (l elem r) #:transparent)

(define t
   (node
     (node (leaf) 2 (leaf))
     5
     (node (node (leaf) 6 (leaf))
            8
            (node (leaf) 9 (leaf)))))

; przechodzenie drzewa z funkcja
(define (fold-tree f x t)
    (cond [(leaf? t) x]
          [(node? t)
           (f
            (fold-tree f x (node-l t))
            (node-elem t)
            (fold-tree f x (node-r t)))]))

; suma wartosci w drzewie
(define (sum-tree t)
  (fold-tree
   (lambda (left elem right) (+ left elem right))
   0
   t))

(sum-tree t)

; odwracanie drzewa
(define (tree-flip t)
  (fold-tree
   (lambda (left elem right) (node right elem left))
   (leaf)
   t))

(tree-flip t)

; najdluzsza galaz drzewa
(define (tree-height t)
  (fold-tree
   (lambda (left elem right) (+ 1 (max left right)))
   0
   t))

(tree-height t)

; najglebsze wartosci drzewa
(define (tree-span t)
  (define (right-val t) ; wartosc najglebiej po prawej
    (if (leaf? (node-r t)) 
        (node-elem t)
        (right-val (node-r t))))
  (define (left-val t) ; wartosc najglebiej po lewej
    (if (leaf? (node-l t)) 
        (node-elem t)
        (left-val (node-l t))))
  (cond [(leaf? t) (list +inf.0 -inf.0)]
        [(node? t) (list (left-val (node-l t)) (right-val (node-r t)))]))

(tree-span t)

; lista z drzewa
(define (flatten t)
  (fold-tree
   (lambda (left elem right)
     (append left (cons elem right)))
   '()
   t))

(flatten t)