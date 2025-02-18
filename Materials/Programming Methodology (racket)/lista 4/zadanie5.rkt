#lang racket
(define-struct leaf () #:transparent)
(define-struct node (l elem r) #:transparent)

; funkcja zwracajaca drzewo jako lista w kolejnosci infiksoweej (z zadania 4)
(define (flat-append t xs)
    (cond [(leaf? t) xs]
          [(node? t) 
            (flat-append    
                (node-l t) 
                (cons (node-elem t) (flat-append (node-r t) xs)))]))

(define (flatten t)
  (flat-append t '()))




(define (insert-bst x t)
  (cond [(leaf? t) (node (leaf) x (leaf))]
        [(node? t)
         (cond  [(= x (node-elem t)) 
                (node  (node-l t) 
                       (node-elem t) 
                       (node (leaf) x (node-r t)))] ; zmiana (mozliwosc tych samych wartosci w drzewie BST)
                [(< x (node-elem t))
                 (node (insert-bst x (node-l t))
                       (node-elem t)
                       (node-r t))]
                [else
                 (node (node-l t)
                       (node-elem t)
                       (insert-bst x (node-r t)))])]))

(define (create-bst xs)
  (foldl insert-bst (leaf) xs)) ; pierwsza wartosc xs jest korzeniem

(create-bst '(7 84 3 2 3 7 9 0 1))

(define (tree-sort xs)
  (flatten (create-bst xs)))

(tree-sort '(7 84 3 2 3 7 9 0 1))

#|
(node
 (node
  (node
   (node
    (leaf) 0 (node (leaf) 1 (leaf))) 2 (leaf)) 3
                                               (node
                                                (leaf) 3 (leaf)))
 7
 (node
  (leaf) 7
  (node
   (node
    (leaf) 9 (leaf)) 84 (leaf))))
|#