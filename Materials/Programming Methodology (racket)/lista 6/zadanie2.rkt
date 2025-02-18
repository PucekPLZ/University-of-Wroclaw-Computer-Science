#lang plait

#|

(define (append xs ys)
   (if (empty? xs)
       ys
       (cons (first xs) (append (rest xs) ys))))

|#

#|

Pokażę za pomocą indukcji, że (append xs ys) ≡ zs dla dowolnych list xs i ys istnieje lista zs.

Podstawa indukcji:
Niech xs będzie listą pustą xs = '(). Czyli (append '() ys) ≡ ys,
to wynika wprost z definicji funkcji append. (Lemat 1 też był w notatce)

Krok indukcyjny:
Założe, że (append xs ys) ≡ zs zachodzi dla dowolnej listy xs.
Pokaże, że (append (cons x xs) ys) ≡ (cons x zs) również zachodzi.

(append (cons x xs) ys) ≡ z def. append
(cons x (append xs ys)) ≡ z założenia indukcyjnego
(cons x zs)

(cons x zs) ≡ (cons x zs)

Więc na mocy indukcji udowodniłem, że (append xs ys) ≡ zs dla dowolnych list xs i ys istnieje zs.

|#