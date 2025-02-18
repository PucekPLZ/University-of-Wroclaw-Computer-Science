#lang racket

(define (partial-sums stream)
  (define (helper s acc)
    (stream-cons acc
                 (helper
                  (stream-rest s)
                  (+ acc (stream-first s)))))
  (helper stream 0))

(define integers ;; strumien liczb 
    (stream-cons 1 (stream-map add1 integers)))

(define partial-sums-stream (partial-sums integers))

(stream-ref partial-sums-stream 0) 
(stream-ref partial-sums-stream 1) 
(stream-ref partial-sums-stream 2) 
(stream-ref partial-sums-stream 3) 
(stream-ref partial-sums-stream 4)

(stream->list (stream-take partial-sums-stream 10))