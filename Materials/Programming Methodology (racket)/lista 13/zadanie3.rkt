#lang racket

;;

(define (map2 f xs ys)
  (stream-cons
   (f (stream-first xs)
      (stream-first ys))
   (map2 f (stream-rest xs) (stream-rest ys))))

;;

(define (factorial-stream)
  (define integers  ;; strumien liczb
    (stream-cons 1 (stream-map add1 integers)))
  (define S
    (stream-cons 1 (map2 * S integers)))
  S)

(define S (factorial-stream))
(stream-ref S 2)
(stream-ref S 3)
(stream-ref S 4)
(stream-ref S 5)

(stream->list (stream-take S 10))
