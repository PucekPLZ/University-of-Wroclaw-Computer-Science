#lang racket

(define (prime? primes n)
  (define (iter stream)
    (cond
      [(zero? (modulo n (stream-first stream))) #f] 
      [(stream-empty? (stream-rest stream)) #t] 
      [else (iter (stream-rest stream))])) 
  (iter primes))

(define (primes)
  (define (generate primes n)
    (if (prime? primes n) 
        (stream-cons n (generate (stream-cons n primes) (+ n 1))) 
        (generate primes (+ n 1)))) 
   (stream-cons 2 (generate (stream-cons 2 (stream)) 3))) ;; zaczecie od 2

(define prime-stream (primes))
(stream->list (stream-take (primes) 10)) 

