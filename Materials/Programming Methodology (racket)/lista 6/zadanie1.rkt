#lang plait

#|

(define (my-map f xs)
  (if (empty? xs)
      empty
      (cons (f (car xs))
            (my-map f (cdr xs)))))

|#

#|

Pokażę za pomocą indukcji, że (map f (map g xs)) ≡ (map (lambda (x) (f (g x))) xs) dla dowolnych funkcji f i g.

Podstawa indukcji:
Niech xs będzie listą pustą xs = '(). Więc obie strony wyrażenia obliczają się do listy pustej,
to wynika wprost z definicji funkcji map.

Krok indukcyjny:
Założe, że (map f (map g ys)) ≡ (map (lambda (x) (f (g x))) ys) zachodzi dla dowolnej listy ys.
Pokaże, że (map f (map g (cons y ys))) ≡ (map (lambda (x) (f (g x))) (cons y ys)) również zachodzi.

Na początku rozpisujemy lewą stronę (map g (cons y ys)

(map f (map g (cons y ys))) ≡ z def. map
(map f (cons (g y) (map g ys))) ≡ z def. map
(cons (f (g y)) (map f (map g ys)))

Teraz zajmę się drugą stroną i rozpisze (map (lambda (x) (f (g x))) (cons y ys))

(map (lambda (x) (f (g x))) (cons y ys)) ≡  z def. map
(cons (f (g y)) (map (lambda (x) (f (g x))) ys))

Pozostaje mi pokazać, że (cons (f (g y)) (map f (map g ys))) ≡ (cons (f (g y)) (map (lambda (x) (f (g x))) ys))

Z założenia indukcyjnego wiem, że (map f (map g ys)) ≡ (map (lambda (x) (f (g x))) ys).
Więc mogę podstawić w lewej stronie (map (lambda (x) (f (g x))) ys) za (map f (map g ys)).

(cons (f (g y)) (map (lambda (x) (f (g x))) ys)) ≡ (cons (f (g y)) (map (lambda (x) (f (g x))) ys))

Więc na mocy indukcji udowodniłem, że (map f (map g xs)) ≡ (map (lambda (x) (f (g x))) xs) dla dowolnej listy xs.

|#