#lang racket

#| (* (+ 2 2) 5) jak jest 20 to nie dziala |#

#| (* (+ 2 2) (5))  (5) to procedura nie argument |#

#| (*(+(2 2) 5)) (2 2) to procedura nie argument |#

#| (*(+ 2
        2) 5) tak samo jak w pierwszym|#

#| (5 * 4) |#

#| (5 * (2 + 2)) |#

#| ((+ 2 3)) |#

#| + |#

(define + (* 2 3) )

+

(* 2 +)

(define (five) 5)

(define four 4)

(five)

four

five

#| (four) |#