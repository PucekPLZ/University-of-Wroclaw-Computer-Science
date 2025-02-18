#lang racket
; <expr> ::= <term> | <expr> "+" <term> | <expr> "-" <term>
; <term> ::= <factor> | <term> "*" <power> | <term> "/" <power>
; <power> ::= <unary> | <power> "^" <unary>
; <unary> ::= <number> | "-" <unary> | "(" <expr> ")" | <unary> "!"

; <number> ::= "0" | "1" | "2" | ...