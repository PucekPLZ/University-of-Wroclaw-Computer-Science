#lang racket

(define (a-plus-abs-b a b)
   ((if (> b 0) +  #| if |#
                -) #| else |#
        a b))

(a-plus-abs-b 1 4)