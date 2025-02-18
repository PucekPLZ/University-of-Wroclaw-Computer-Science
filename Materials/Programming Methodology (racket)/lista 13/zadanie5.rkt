#lang racket

(define (merge s1 s2)
  (let [(x1 (stream-first s1))
        (x2 (stream-first s2))]
    (cond
      [(= x1 x2) (stream-cons x1 (merge (stream-rest s1) (stream-rest s2)))] 
      [(< x1 x2) (stream-cons x1 (merge (stream-rest s1) s2))] 
      [(> x1 x2) (stream-cons x2 (merge s1 (stream-rest s2)))])))

(define (scale n s)
  (if (stream-empty? s)
      (stream)
      (stream-cons (* n (stream-first s)) (scale n (stream-rest s)))))  

(define (hamming)
  (define hamming-stream
    (stream-cons 1
                 (merge (scale 2 hamming-stream) 
                        (merge (scale 3 hamming-stream) 
                               (scale 5 hamming-stream))))) 
  (stream-rest hamming-stream))

(define hamming-sequence (hamming))
(stream->list (stream-take hamming-sequence 10))


