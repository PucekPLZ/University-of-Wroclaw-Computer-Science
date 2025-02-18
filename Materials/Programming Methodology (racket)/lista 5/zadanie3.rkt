#lang plait

(define (apply f x)
  (f x))

(define (compose f g)
  (lambda (x)
    (f (g x))))

(define (flip f)
  (lambda (x y)
    (f y x)))

(define (curry f)
  (lambda (x)
    (lambda (y)
      (f x y))))
#|
( curry compose )
Ta procedura stosuje funkcję curry do compose
która zwraca nową funkcję, która przyjmuje pojedynczy argument x i zwraca nową funkcję która składa dwie funkcje przekazane jako argumenty do curry
(('_a -> '_b) -> (('_c -> '_a) -> ('_c -> '_b)))
|#


#|
(( curry compose ) ( curry compose ) )
Ta procedura stosuje funkcję curry do compose
która zwraca nową funkcję, która przyjmuje pojedynczy argument x i zwraca nową funkcję która składa dwie funkcje przekazane jako argumenty do curry
Gdy zastosujemy tę nową funkcję do (curry compose) otrzymamy nową funkcję która przyjmuje pojedynczy argument x i zwraca funkcję która składa dwie funkcje przekazane do (curry compose)
(('_a -> ('_b -> '_c)) -> ('_a -> (('_d -> '_b) -> ('_d -> '_c))))
|#

#|
(( curry compose ) ( curry apply ) )
Ta procedura stosuje funkcję curry do compose
która zwraca nową funkcję, która przyjmuje pojedynczy argument x i zwraca nową funkcję, która składa dwie funkcje przekazane jako argumenty do curry
Gdy zastosujemy tę nową funkcję do (curry apply) otrzymamy nową funkcję, która przyjmuje pojedynczy argument x i zwraca funkcję która stosuje funkcję przekazaną do (curry apply) do wyniku działania funkcji
do (curry apply) do wyniku zastosowania innej funkcji przekazanej do (curry apply) do x
(('_a -> ('_b -> '_c)) -> ('_a -> ('_b -> '_c)))
|#

#|
(( curry apply ) ( curry compose ) )
Procedura ta stosuje funkcję curry do apply która zwraca nową funkcję przyjmującą pojedynczy argument x i
zwraca nową funkcję która stosuje funkcję przekazaną jako drugi argument do apply do x, gdzie sama funkcja jest przekazana jako pierwszy argument do apply
Gdy zastosujemy tę nową funkcję do (curry compose) otrzymamy nową funkcję która przyjmuje pojedynczy argument x i zwraca wynik zastosowania wyniku zastosowania (curry compose) do x do x
(('_a -> '_b) -> (('_c -> '_a) -> ('_c -> '_b)))
|#

#|
( compose curry flip )
Ta procedura stosuje compose do curry i flip która zwraca nową funkcję która przyjmuje pojedynczy argument x i zwraca funkcję która przyjmuje pojedynczy argument y
i stosuje flip do wyniku zastosowania curry do x i y
(('_a '_b -> '_c) -> ('_b -> ('_a -> '_c)))
|#

#|
'a oznacza tutaj typ polimorficzny, czyli na przykład id jest typu ('a -> 'a), co oznacza "dla dowolnego typu, oznaczmy go jako 'a, możesz traktować funkcję id jako typu ('a -> 'a)"
czyli w pewnym sensie id może mieć tyle różnych typów, ile ci się tylko wymarzy
natomiast jako '_a plait oznacza typ monomorficzny, czyli już wartość, która z całą pewnością jest jednego, konkretnego typu, ale jeszcze nie wiemy jakiego
ogółem jest tak, że z różnych przyczyn typy polimorficzne mogą mieć tylko funkcje - wszystkie inne wartości mają konkretne typy
|#
