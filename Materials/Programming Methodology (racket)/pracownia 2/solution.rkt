#lang racket
(require data/heap)

(struct sim ([time #:mutable] events))
(struct wire (sim [value #:mutable] [actions #:mutable]))
(struct action (out in1 in2 proc))

(provide sim? wire?
         (contract-out
          [make-sim        (-> sim?)]
          [sim-wait!       (-> sim? positive? void?)]
          [sim-time        (-> sim? real?)]
          [sim-add-action! (-> sim? positive? (-> any/c) void?)]

          [make-wire       (-> sim? wire?)]
          [wire-on-change! (-> wire? (-> any/c) void?)]
          [wire-value      (-> wire? boolean?)]
          [wire-set!       (-> wire? boolean? void?)]

          [bus-value (-> (listof wire?) natural?)]
          [bus-set!  (-> (listof wire?) natural? void?)]

          [gate-not  (-> wire? wire? void?)]
          [gate-and  (-> wire? wire? wire? void?)]
          [gate-nand (-> wire? wire? wire? void?)]
          [gate-or   (-> wire? wire? wire? void?)]
          [gate-nor  (-> wire? wire? wire? void?)]
          [gate-xor  (-> wire? wire? wire? void?)]

          [wire-not  (-> wire? wire?)]
          [wire-and  (-> wire? wire? wire?)]
          [wire-nand (-> wire? wire? wire?)]
          [wire-or   (-> wire? wire? wire?)]
          [wire-nor  (-> wire? wire? wire?)]
          [wire-xor  (-> wire? wire? wire?)]

          [flip-flop (-> wire? wire? wire? void?)]))

;; Symulacja

(define (make-sim)
  (sim 0 (make-heap (lambda (pair1 pair2) (< (car pair1) (car pair2))))))

(define (execute-action! action)
  (if (null? (action-in2 action))
      (wire-set!
       (action-out action)
       ((action-proc action)
        (wire-value (action-in1 action))))
  (wire-set! (action-out action)
   ((action-proc action)
    (wire-value (action-in1 action))
    (wire-value (action-in2 action))))))

(define (sim-wait! sim time)
  (define end-time (+ (sim-time sim) time))
  (define (execute-next-action)
    (let ([heap (sim-events sim)])
      (when (> (heap-count heap) 0)
        (let* ([action-record (heap-min heap)]
               [action-time (car action-record)]
               [action (cdr action-record)])
          (when (<= action-time end-time)
            (begin (heap-remove-min! heap)
                   (set-sim-time! sim action-time)
                   (execute-action! action)
                   (execute-next-action)))))))
  (begin (execute-next-action) (set-sim-time! sim end-time)))

(define (sim-add-action! sim time action)
  (heap-add! (sim-events sim) (cons time action)))

;; Przewody
                        
(define (make-wire sim)
  (wire sim #f '()))

(define (wire-on-change! wire action-record)
  (begin (set-wire-actions! wire (cons action-record (wire-actions wire)))
         (execute-action! (cdr action-record))))

(define (add-actions! wire)
  (let* ([sim (wire-sim wire)] [time (sim-time sim)])
    (for-each
     (lambda (action-record)
       (sim-add-action! sim (+ time (car action-record)) (cdr action-record)))
     (wire-actions wire))))

(define (wire-set! wire value)
  (when (not (eq? (wire-value wire) value))
    (begin (set-wire-value! wire value) (add-actions! wire))))

;; Bramki logiczne 

(define (gate-helper out in1 in2 proc wait-time)
  (wire-on-change! in1 (cons wait-time (action out in1 in2 proc)))
  (when (not (null? in2))
    (wire-on-change! in2 (cons wait-time (action out in1 in2 proc)))))

(define (gate-not out in)
  (gate-helper out in null not 1))

(define (gate-and out in1 in2)
  (gate-helper out in1 in2 (lambda (x y) (and x y)) 1))

(define (gate-nand out in1 in2)
  (gate-helper out in1 in2 (lambda (x y) (not (and x y))) 1))

(define (gate-or out in1 in2)
  (gate-helper out in1 in2 (lambda (x y) (or x y)) 1))

(define (gate-nor out in1 in2)
  (gate-helper out in1 in2 (lambda (x y) (not (or x y))) 1))

(define (gate-xor out in1 in2)
  (gate-helper out in1 in2 (lambda (x y) (not (eq? x y))) 2))

(define (wire-helper gate-op in1 in2)
  (define new-wire (make-wire (wire-sim in1)))
  (gate-op new-wire in1 in2)
  new-wire)

(define (wire-not in)
  (define new-wire (make-wire (wire-sim in)))
  (gate-not new-wire in)
  new-wire)

(define (wire-and in1 in2)
  (wire-helper gate-and in1 in2))

(define (wire-or in1 in2)
  (wire-helper gate-or in1 in2))

(define (wire-nor in1 in2)
  (wire-helper gate-nor in1 in2))

(define (wire-nand in1 in2)
  (wire-helper gate-nand in1 in2))

(define (wire-xor in1 in2)
  (wire-helper gate-xor in1 in2))

;;

(define (bus-set! wires value)
  (match wires
    ['() (void)]
    [(cons w wires)
     (begin
       (wire-set! w (= (modulo value 2) 1))
       (bus-set! wires (quotient value 2)))]))

(define (bus-value ws)
  (foldr (lambda (w value) (+ (if (wire-value w) 1 0) (* 2 value)))
         0
         ws))

(define (flip-flop out clk data)
  (define sim (wire-sim data))
  (define w1  (make-wire sim))
  (define w2  (make-wire sim))
  (define w3  (wire-nand (wire-and w1 clk) w2))
  (gate-nand w1 clk (wire-nand w2 w1))
  (gate-nand w2 w3 data)
  (gate-nand out w1 (wire-nand out w3)))
