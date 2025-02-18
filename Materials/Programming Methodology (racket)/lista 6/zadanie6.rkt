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

(define formula
  (conj [var 'C] (disj [var 'A] (neg [var 'B]))))

(to-nnf formula)