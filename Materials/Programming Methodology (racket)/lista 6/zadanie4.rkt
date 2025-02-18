#lang plait

(define-type (NNF 'v)
   (nnf-lit [polarity : Boolean] [var : 'v])
   (nnf-conj [l : (NNF 'v)] [r : (NNF 'v)])
   (nnf-disj [l : (NNF 'v)] [r : (NNF 'v)]))

(define (neg-nnf f)
  (cond
    [(nnf-lit? f) (nnf-lit (not (nnf-lit-polarity f)) (nnf-lit-var f))]
    [(nnf-disj? f)  (nnf-conj (neg-nnf (nnf-disj-r f)) (neg-nnf (nnf-disj-l f)))]
    [else  (nnf-disj (neg-nnf (nnf-conj-r f)) (neg-nnf (nnf-conj-l f)))]))

#|

Pokaże, że (neg-nnf (neg-nnf φ)) ≡ φ dla dowolnej formuły φ w NNF.

Podstawa indukcji:
Założe, że φ jest literałem w postaci (nnf-lit polarity var). 

1) Jeżeli polarity jest prawdą, wtedy φ jest prawdziwe, to

(neg-nnf (neg-nnf φ)) ≡ z założenia, że polarity jest prawdą
(neg-nnf (neg-nnf (nnf-lit #t var))) ≡ z def. neg-nnf na literałach
(nnf-lit (nnf-lit #f var)) ≡ z def. neg-nnf na literałach
(nnf-lit #t val) ≡ z założenia, że polarity jest prawdą
φ

2) Jeżeli polarity jest fałszem, wtedy φ jest fałszywe, to 

(neg-nnf (neg-nnf φ)) ≡ z założenia, że polarity jest fałszem
(neg-nnf (neg-nnf (nnf-lit #f var))) ≡ z def. neg-nnf na literałach
(nnf-lit (nnf-lit #t var)) ≡ z def. neg-nnf na literałach
(nnf-lit #f var) ≡ z założenia, że polarity jest fałszywe
φ

(neg-nnf (neg-nnf φ)) ≡ φ zachodzi dla dowolnego wartościowania polarity.

Krok indukcyjny:
Założe, że φ jest formułą w postaci (nnf-conj l r) lub (nnf-disj l r).

1) Jeżeli φ jest postaci (nnf-conj l r) to

(neg-nnf (neg-nnf φ)) ≡ z założenia, że φ jest postaci (nnf-conj l r)
(neg-nnf (neg-nnf (nnf-conj l r))) ≡ z def. neg-nnf na koniunkcji
(neg-nff (nnf-disj (neg-nnf l) (neg-nnf r))) ≡ z def. neg-nnf na dysjunkcji
(neg-conj (neg-nnf (neg-nnf l)) (neg-nnf (neg-nnf r)))) ≡ z założenia indukcyjnego (neg-nnf (neg-nnf φ)) ≡ φ
(neg-conj l r) ≡ z założenia, że φ jest postaci (nnf-conj l r)
φ

2) Jeżeli φ jest postaci (nnf-disj l r) to

(neg-nnf (neg-nnf φ)) ≡ z założenia, że φ jest postaci (nnf-disj l r)
(neg-nnf (neg-nnf (nnf-disj l r))) ≡ z def. neg-nnf na disjunkcija
(neg-nff (nnf-conj (neg-nnf l) (neg-nnf r))) ≡ z def. neg-nnf na koniunkcji
(neg-disj (neg-nnf (neg-nnf l)) (neg-nnf (neg-nnf r)))) ≡ z założenia indukcyjnego (neg-nnf (neg-nnf φ)) ≡ φ
(neg-disj l r) ≡ z założenia, że φ jest postaci (nnf-disj l r)
φ

Więc na mocy indukcji udowodniłem, że dla dowolnej formuły φ w NNF zachodzi (neg-nnf (neg-nnf φ)) ≡ φ.

|#