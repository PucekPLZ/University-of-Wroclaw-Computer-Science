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

; funkcja znajdujaca maksymalny lewy element, czyli minimum BST (z zadania 2)
(define (left-val t)
    (if (leaf? (node-l t)) 
        (node-elem t)
        (left-val (node-l t))))

; funkcja usuwająca
(define (delete-bst x t)
  (cond [(leaf? t) t] ; jeśli t jest lisciem - zwróć drzewo bez zmian, nie ma w nim x
        [(node? t)
         (cond  [(= x (node-elem t))  ; x jest w drzewie
                    (cond 
                        [(and (leaf? (node-l t)) (leaf? (node-r t))) ; jak nie ma dzieci to zamienia sie w liscia
                            (leaf)] 
                        [(leaf? (node-l t)) ; jeśli ma tylko prawe dziecko, zwracamy je
                            (node-r t)] 
                        [(leaf? (node-r t)) ; jeśli ma tylko lewe dziecko, zwracamy je
                            (node-l t)] 
                        [else ; jeśli ma dwójke dzieci 
                            (let ([newx (left-val (node-r t))]) ; newx - min z prawego poddrzewa, czyli najmniejszy element wiekszy od x
                            (node 
                                (node-l t) ; lewe bez zmian
                                newx ; najmniejszy element wiekszy od x
                                (delete-bst newx (node-r t))))])] ; prawe z usunietym newx
                [(< x (node-elem t)) 
                 (node (delete-bst x (node-l t)) 
                       (node-elem t)
                       (node-r t))]
                [else
                 (node (node-l t)
                       (node-elem t) 
                       (delete-bst x (node-r t)))])]))

(delete-bst 5 t)
(delete-bst 2 t)
(delete-bst 9 t)