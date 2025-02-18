#lang plait

(define-type (NNF 'v)
   (nnf-lit [polarity : Boolean] [var : 'v])
   (nnf-conj [l : (NNF 'v)] [r : (NNF 'v)])
   (nnf-disj [l : (NNF 'v)] [r : (NNF 'v)]))

(define-type (Formula 'v)
   (var [var : 'v])
   (neg [f : (Formula 'v)])
   (conj [l : (Formula 'v)] [r : (Formula 'v)])
   (disj [l : (Formula 'v)] [r : (Formula 'v)]))

(define (neg-nnf f)
  (cond
    [(nnf-lit? f) (nnf-lit (not (nnf-lit-polarity f)) (nnf-lit-var f))]
    [(nnf-disj? f)  (nnf-conj (neg-nnf (nnf-disj-r f)) (neg-nnf (nnf-disj-l f)))]
    [else  (nnf-disj (neg-nnf (nnf-conj-r f)) (neg-nnf (nnf-conj-l f)))]))

(define (to-nnf form)
  (cond
    [(var? form) (nnf-lit #t (var-var form))]
    [(conj? form) (nnf-conj (to-nnf (conj-l form)) (to-nnf (conj-r form)))]
    [(disj? form) (nnf-disj (to-nnf (disj-l form)) (to-nnf (disj-r form)))]
    [else (neg-nnf (to-nnf (neg-f form)))]))

(define (σ var)
  (cond [(equal? var 'x) #t] 
        [(equal? var 'y) #f] 
        [else #t])) 
        
(define (eval-nnf σ f)
  (if (nnf-lit? f)
      (if (nnf-lit-polarity f)
          (σ (nnf-lit-var f))
          (not (σ (nnf-lit-var f))))
      (if (nnf-conj? f)
          (and (eval-nnf σ (nnf-conj-l f)) (eval-nnf σ (nnf-conj-r f)))
          (or (eval-nnf σ (nnf-disj-l f)) (eval-nnf σ (nnf-disj-r f))))))
#|

(define (eval-formula σ fo)
  (eval-nnf σ (to-nnf fo)))

|#

(define (eval-formula σ fo)
  (if (var? fo)
     (σ (var-var fo))
      (cond
        [(neg? fo) (not (eval-formula σ (neg-f fo)))]
        [(conj? fo) (and (eval-formula σ (conj-l fo)) (eval-formula σ (conj-r fo)))]
        [(disj? fo) (or (eval-formula σ (disj-l fo)) (eval-formula σ (disj-r fo)))])))

#|

Pokaże, że (eval-nnf σ (to-nnf φ)) ≡ (eval-formula σ φ) dla dowolnej formuły φ i wartościowania σ.

Podstawa indukcji:
Niech φ będzie dowolną zmienną ('x) i σ dowolnym wartościowaniem, to

(eval-formula σ φ) ≡ z założenia
(eval-formula σ (var 'x)) ≡ z def. eval-formula
(σ 'x)

Druga strona

(eval-nnf σ (to-nnf φ)) ≡ z założenia
(eval-nnf σ (to-nnf (var 'x))) ≡ z def. to-nnf
(eval-nnf σ (nnf-lit #t 'x)) ≡ z def. eval-nnf
(σ 'x)

Więc (σ 'x) ≡ (σ 'x)

Krok indukcjyjny:
Niech Ψ i φ to dowolne formuły i σ dowolne wartościowanie.
Założe, że (eval-formula σ φ) = (eval-nnf σ (to-nnf φ)) oraz (eval-formula σ Ψ) = (eval-nnf σ (to-nnf Ψ))

1) Koniunkcja

(eval-formula σ (conj φ Ψ) ≡ z def. eval-formula
(and (eval-formula σ φ) (eval-formula σ Ψ)) ≡ z założenia
(and (eval-nnf σ (to-nnf φ)) (eval-nnf σ (to-nnf Ψ))) ≡ z def. eval-nnf (w druga stronę)
(eval-nnf σ (nnf-conj (to-nnf φ) (to-nnf Ψ))) ≡ z def. to-nnf (w druga stronę)
(eval-nnf σ (to-nnf (conj φ Ψ)))

2) Dla disjunkcji podobnie.

3) Negacja

(eval-nnf σ (to-nnf (neg φ))) ≡ z def. to-nnf
(not (eval-nnf σ (to-nnf φ))) ≡ z założenia
(not (eval-formula σ φ))

Druga strona

(eval-formula σ (neg φ)) ≡ z def. eval-formula
(not (eval-formula σ φ))

Więc (not (eval-formula σ φ)) ≡ (not (eval-formula σ φ)).

Zatem na mocy indukcji udowodniłem, że (eval-nnf σ (to-nnf φ)) ≡ (eval-formula σ φ).

|#
















