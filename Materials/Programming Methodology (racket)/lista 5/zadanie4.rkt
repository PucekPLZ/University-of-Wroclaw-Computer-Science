#lang plait

(define (remove x lst)
  (filter (lambda (y) (not (eq? x y))) lst))

(define (helper f lst)
  (foldl (lambda (x acc) (append (f x) acc)) '() lst))

(define (perms lst)
  (if (empty? lst)
      (list '())
      (helper (lambda (x)
                 (map (lambda (p) (cons x p))
                      (perms (remove x lst))))
               lst)))


(perms '(1 2 3))

