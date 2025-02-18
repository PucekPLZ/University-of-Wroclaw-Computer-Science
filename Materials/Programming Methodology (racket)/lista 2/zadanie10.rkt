#lang racket
(provide merge-sort)

(define (split xs)
  (if (even? (length xs))
      (let-values (((head tail) (split-at xs (/ (length xs) 2)))) (list head tail))
      (let-values (((head tail) (split-at xs (/ (- (length xs) 1) 2)))) (list head tail))))

(define (merge xs ys)
  (cond [(null? xs)
         ys]
        [(null? ys)
         xs]
        [(<= (car xs) (car ys))
         (cons (car xs) (merge (cdr xs) ys))]
        [else
         (cons (car ys) (merge xs (cdr ys)))]))

(define (tail xs)
    (car (cdr xs)))

(define (merge-sort xs)
  (if (<= (length xs) 1)
       xs
      (merge (merge-sort (car (split xs))) (merge-sort (tail (split xs))))))

(define lst (list 7 6 2 3 1 2 0 0 -10 9))

(merge-sort lst)

; jest strukturalnie rekurecyjna