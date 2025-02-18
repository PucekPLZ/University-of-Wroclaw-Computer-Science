#lang plait

(define (sorted? xs)
  (cond [(or (empty? xs) (empty? (rest xs))) #t]
        [(> (first xs) (first(rest xs))) #f]
        [else (sorted? (rest xs))]))
        
(define (insert x xs)
  (cond [(empty? xs) (cons x (list))]
        [(> (first xs) x) (cons x xs)]
        [else (cons (first xs) (insert x (rest xs)))]))

#|

Pokaże, że jeśli (sorted? xs) ≡ #t to (sorted? (insert x xs)) ≡ #t.

Podstawa indukcji:
Niech xs będzie listą pustą xs = '().

(sorted? xs) ≡
(sorted? '()) ≡
#t

To wynika z tego, że lista pusta jest posortowana.

(sorted? (insert x xs)) ≡ z def. insert
(sorted? (cons x xs)) ≡
(sorted? (cons x '())) ≡
#t

To wynika z tego, że lista jednoelementowa jest posortowana.

Krok indukcyjny:
Założe, że (sorted? xs) ≡ #t to (sorted? (insert x xs)) ≡ #t zachodzi dla każdej listy od długości n lub mniejszej.
Pokaże, że (sorted? xs) ≡ #t to (sorted? (insert x xs)) ≡ #t zachodzi dla każdej listy od długości n+1. 

Niech xs = (cons y ys), gdzie y to pierwszy element xs, a ys to reszta listy xs.
Skoro (sorted? xs) ≡ #t, to y <= (first ys).

Teraz rozważe (sorted? (insert x xs)) ≡ #t.

1) Jeżeli x <= y, to
(sorted? (insert x xs)) ≡ z def. insert (dodaje na początek listy, bo x jest mniejsze od pierwszego elementu xs)
(sorted? (cons x xs)) ≡ z def. insert (dodaje element do listy posortowanej) 
#t (skoro xs jest posortowane to, jeżeli dodam na początek xs element mniejszy lub równy pierwszemu elementu xs to nadal będzie posortowana)

2) Jeżeli x > y, to 
(sorted? (insert x xs)) ≡ z def. insert (dodaje po y do listy, i szukam odpowiedniego miejsca dla x)
(sorted? (cons y (insert x ys))) ≡ z założenia indukcyjnego ((insert x ys) jest posortowane bo, y <= (first ys), więc y <= x)
#t

Więc na mocy indukcji udowodniłem, że jeśli (sorted? xs) ≡ #t to (sorted? (insert x xs)) ≡ #t.

|#