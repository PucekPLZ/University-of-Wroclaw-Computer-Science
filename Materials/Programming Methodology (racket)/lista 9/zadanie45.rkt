#lang racket
(require rackunit)

(define morse-list
  '((#\A . "._")   (#\B . "_...") (#\C . "_._.") (#\D . "_..")
    (#\E . ".")    (#\F . ".._.") (#\G . "__.")  (#\H . "....")
    (#\I . "..")   (#\J . ".___") (#\K . "_._")  (#\L . "._..")
    (#\M . "__")   (#\N . "_.")   (#\O . "___")  (#\P . ".__.") 
    (#\Q . "__._") (#\R . "._.")  (#\S . "...")  (#\T . "_")
    (#\U . ".._")  (#\V . "..._") (#\W . ".__")  (#\X . "_.._")
    (#\Y . "_.__") (#\Z . "__..")
    (#\a . "._")   (#\b . "_...") (#\c . "_._.") (#\d . "_..")
    (#\e . ".")    (#\f . ".._.") (#\g . "__.")  (#\h . "....")
    (#\i . "..")   (#\j . ".___") (#\k . "_._")  (#\l . "._..")
    (#\m . "__")   (#\n . "_.")   (#\o . "___")  (#\p . ".__.") 
    (#\q . "__._") (#\r . "._.")  (#\s . "...")  (#\t . "_")
    (#\u . ".._")  (#\v . "..._") (#\w . ".__")  (#\x . "_.._")
    (#\y . "_.__") (#\z . "__..")
    (#\0 . "_____") (#\1 . ".____") (#\2 . "..___") (#\3 . "...__")
    (#\4 . "...._") (#\5 . ".....") (#\6 . "_....") (#\7 . "__...")
    (#\8 . "___..") (#\9 . "____.")
    (#\, . "__..__") (#\; . "_._._.") (#\? . "..__..")
    (#\: . "___...") (#\' . ".____.") (#\- . "_...._") 
    (#\/ . "_.._.")  (#\space . " ")  (#\. . "._._._")
    (#\+ . "._._.")  (#\* . "_._.")   (#\@ . ".__.__.") 
    (#\= . "_..._")))

(define (morse-get char)
  (define (it morse-list)
    (cond
      [(null? morse-list) "*"]
      [(equal? (car (car morse-list)) char) (cdr (car morse-list))]
      [else (it (cdr morse-list))]))
  (it morse-list))

(define (morse-code string)
  (let ([charlist (string->list string)])
    (define (it charlist result)
      (if (null? charlist)
          (string-join (reverse result))
          (it (cdr charlist) (cons (morse-get (car charlist)) result))))
    (it charlist '())))

(morse-code "Metody Programowania")
(check-equal? "__ . _ ___ _.. _.__   .__. ._. ___ __. ._. ._ __ ___ .__ ._ _. .. ._" (morse-code "Metody Programowania"))

(define (char-get char)
  (define (it morse-list)
    (cond
      [(null? morse-list) #\*]
      [(equal? (cdr (car morse-list)) char) (car (car morse-list))]
      [else (it (cdr morse-list))]))
  (if (equal? char "")
      #\space
      (it morse-list)))

(define (morse-decode string)
  (let ([morselist (string-split string " ")])
    (define (it morselist result)
      (if (null? morselist)
          (list->string (reverse result))
          (it (cdr morselist) (cons (char-get (car morselist)) result))))
    (it morselist '())))

(morse-code "MP 2022")
(morse-decode "__ .__.  ..___ _____ ..___ ..___") 