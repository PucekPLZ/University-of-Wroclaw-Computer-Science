#lang racket

(define (val a b)
     (or (and (> a b) a)  b))   #| (or (and ifCond ifTrue) (or ifCond ifFalse)) |#


(val 12 11)


