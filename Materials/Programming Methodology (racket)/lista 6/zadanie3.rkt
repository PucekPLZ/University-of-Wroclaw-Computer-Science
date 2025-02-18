#lang plait

(define-type (NNF 'v)
   (nnf-lit [polarity : Boolean] [var : 'v])
   (nnf-conj [l : (NNF 'v)] [r : (NNF 'v)])
   (nnf-disj [l : (NNF 'v)] [r : (NNF 'v)]))

#|

Flaga polarity w konstruktorze literału oznacza, czy zmienna jest zanegowana
(wartość #f), czy nie (wartość #t). Sformułuj zasadę indukcji dla typu NNF.

|#


#|

Dowolna formuła NNF może być zbudowana za pomocą tylko koniunkcji, alternatywy i literałów,
gdzie literały to zanegowane lub nie zanegowane zmienne zdaniowe.
Dlatego, aby pokazać, że dowolna formuła NNF jest w NNF, muszę pokazać,
że literały są w NNF oraz, że jeśli połączę dwie formuły NNF używając koniunkcji lub dysjunkcji,
to otrzymana formuła jest również w NNF.

Podstawa indukcji:
1) Dla nnf-lit gdy var jest zmienną bez negacji, czyli polarity jest prawdą.
2) Dla nnf-lit gdy var jest zmienną z negacji, czyli polarity jest fałszem.

Krok indukcyjny:
1) Dla nnf-conj, zakładam, że indukcja zachodzi dla lewej i prawej strony, oraz lewa i prawa strona są w NNF.
Muszę pokazać, że nnf-conj do lewej i prawej strony także jest w NNF.
1) Dla nnf-disj, zakładam, że indukcja zachodzi dla lewej i prawej strony, oraz lewa i prawa strona są w NNF.
Muszę pokazać, że nnf-disj do lewej i prawej strony także jest w NNF.

Zasada indukcji:
Dla dowolnej formuły φ w NNF, jeżeli wszystko zachodzi:
- φ jest (nnf-lit #t var), to φ jest w NNF
- φ jest (nnf-lit #f var), to φ jest w NNF
- φ jest (nnf-conj l r), gdzie l i r są w NNF, to (nnf-conj l r) jest w NNF
- φ jest (nnf-disj l r), gdzie l i r są w NNF, to (nnf-disj l r) jest w NNF
To φ jest w NNF.

|#