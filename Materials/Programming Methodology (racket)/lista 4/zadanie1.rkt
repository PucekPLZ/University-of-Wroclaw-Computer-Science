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