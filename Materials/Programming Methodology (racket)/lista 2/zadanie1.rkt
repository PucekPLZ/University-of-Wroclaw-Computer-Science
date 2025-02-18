#lang racket

(let ([x 3])  ; x wiazaca
  (+ x y))    ; x zwiazana y wolna


(let ([x 1]           ; x wiazaca
      [y (+ x 2)])    ; y wiazaca x wolna
   (+ x y))           ; y zwiazana x zwiazana

(let ([x 1])             ; x wiazaca
  (let ([y (+ x 2)])     ; y wiazaca x zwiazana
    (* x y)))            ; x zwiazana y zwiazana

(define (f x y)    ; x wiazaca y wiazaca 
   (* x y z))      ; x zwiazana y zwiazana z wolna

(define (f x)           ; x wiazaca
   (define (g y z)      ; y wiazaca z wiazaca
      (* x y z))        ; x zwiazana y zwiazana z zwiazana
   (f x x x ))          ; x zwiazana