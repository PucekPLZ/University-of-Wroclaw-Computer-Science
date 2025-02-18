#lang plait

(define-type (NNF 'v)
   (nnf-lit [polarity : Boolean] [var : 'v])
   (nnf-conj [l : (NNF 'v)] [r : (NNF 'v)])
   (nnf-disj [l : (NNF 'v)] [r : (NNF 'v)]))

#|

(define (σ var)
  (cond [(equal? var 'x) #t] 
        [(equal? var 'y) #f] 
        [else #t]))

|#

(define (eval-nnf σ f)
  (if (nnf-lit? f)
      (if (nnf-lit-polarity f)
          (σ (nnf-lit-var f))
          (not (σ (nnf-lit-var f))))
      (if (nnf-conj? f)
          (and (eval-nnf σ (nnf-conj-l f)) (eval-nnf σ (nnf-conj-r f)))
          (or (eval-nnf σ (nnf-disj-l f)) (eval-nnf σ (nnf-disj-r f))))))

(define (neg-nnf f)
  (cond
    [(nnf-lit? f) (nnf-lit (not (nnf-lit-polarity f)) (nnf-lit-var f))]
    [(nnf-disj? f)  (nnf-conj (neg-nnf (nnf-disj-r f)) (neg-nnf (nnf-disj-l f)))]
    [else  (nnf-disj (neg-nnf (nnf-conj-r f)) (neg-nnf (nnf-conj-l f)))]))


#|

Pokaże, że dla dowolnej formuły φ i wartościowania σ zachodzi (eval-nnf σ (neg-nnf φ)) ≡ (not (eval-nnf σ φ)).

Podstawa indukcji:
Założe, że φ jest literałem w postaci (nnf-lit polarity var).

1) Rozważam przypadek bez negacji dla φ = (nnf-lit #t 'x), to

(eval-nnf σ (neg-nnf φ)) ≡ z założenia, że φ = (nnf-lit #t 'x)
(eval-nnf σ (neg-nnf (nnf-lit #t 'x))) ≡ z def. neg-nnf
(eval-nnf σ (nnf-lit #f 'x)) ≡ z def. eval-nnf
(not (σ 'x))

Druga strona

(not (eval-nnf σ (nnf-lit #t 'x))) ≡ z def. eval-nnf
(not (σ 'x))

Więc (not (σ 'x)) ≡ (not (σ 'x))

2) Rozważam przypadek bez negacji dla φ = (nnf-lit #t 'y), to

(eval-nnf σ (neg-nnf φ)) ≡ z założenia, φ = (nnf-lit #t 'y)
(eval-nnf σ (neg-nnf (nnf-lit #t 'y))) ≡ z def. neg-nnf
(eval-nnf σ (nnf-lit #t 'y)) ≡ z def. eval-nnf
(not (σ 'y))

Druga strona

(not (eval-nnf σ (nnf-lit #t 'y))) ≡ z def. eval-nnf
(not (σ 'y))

Więc (not (σ 'y)) ≡ (not (σ 'y))

3) Rozważam przypadek z negacją dla φ = (nnf-lit #f 'x), to

(eval-nnf σ (neg-nnf φ)) ≡ z założenia, że φ = (nnf-lit #f 'x)
(eval-nnf σ (neg-nnf (nnf-lit #f 'x))) ≡ z def. neg-nnf
(eval-nnf σ (nnf-lit #t 'x)) ≡ z def. eval-nnf
(σ 'x)

Druga strona

(not (eval-nnf σ (nnf-lit #f 'x))) ≡ z def. eval-nnf
(not (not (σ 'x))) ≡ zasada podwójnej negacji
(σ 'x)

Więc (σ 'x) ≡ (σ 'x)
Podobnie dla φ = (nnf-lit #f 'y) drugiego wartościowania.

Krok indukcyjny:
Założe, że φ jest formułą w postaci (nnf-conj l r) lub (nnf-disj l r).
Założe, że ((eval-nnf σ (neg-nnf l)) ≡ (not (eval-nnf σ l)) oraz (eval-nnf σ (neg-nnf r)) ≡ (not (eval-nnf σ r))).

1) Jeżeli φ jest postaci (nnf-conj l r), to

(eval-nnf σ (neg-nnf φ)) ≡ z założenia, że φ jest postaci (nnf-conj l r)
(eval-nnf σ (neg-nnf (nnf-conj l r))) ≡ z def. neg-nnf
(eval-nnf σ (nnf-disj (neg-nnf l) (neg-nnf r))) ≡ z def. eval-nnf
(or (eval-nnf σ (neg-nnf l)) (eval-nnf σ (neg-nnf r))) ≡ z założenia indukcyjnego 
(or (not (eval-nnf σ l)) (not (eval-nnf σ r))) ≡ z def. eval-nnf (w drugą stronę)
(not (eval-nnf σ (nnf-conj l r))) ≡ z założenia, że φ jest postaci (nnf-conj l r)
(not (eval-nnf σ φ))

Więc (not (eval-nnf σ φ)) ≡ (not (eval-nnf σ φ)) co chciałem pokazać.
Dla disjunkcji podobnie.

Zatem na mocy indukcji dla dowolnej formuły φ i wartościowania σ zachodzi (eval-nnf σ (neg-nnf φ)) ≡ (not(eval-nnf σ φ)).

|#