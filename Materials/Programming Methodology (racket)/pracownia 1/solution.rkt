#lang racket
(provide (struct-out column-info)
         (struct-out table)
         (struct-out and-f)
         (struct-out or-f)
         (struct-out not-f)
         (struct-out eq-f)
         (struct-out eq2-f)
         (struct-out lt-f)
         table-insert
         table-project
         table-sort
         table-select
         table-rename
         table-cross-join
         table-natural-join)

(define-struct column-info (name type) #:transparent)

(define-struct table (schema rows) #:transparent)

(define cities
  (table
   (list (column-info 'city    'string)
         (column-info 'country 'string)
         (column-info 'area    'number)
         (column-info 'capital 'boolean))
   (list (list "Wrocław" "Poland"  293 #f)
         (list "Warsaw"  "Poland"  517 #t)
         (list "Poznań"  "Poland"  262 #f)
         (list "Berlin"  "Germany" 892 #t)
         (list "Munich"  "Germany" 310 #f)
         (list "Paris"   "France"  105 #t)
         (list "Rennes"  "France"   50 #f))))

(define countries
  (table
   (list (column-info 'country 'string)
         (column-info 'population 'number))
   (list (list "Poland" 38)
         (list "Germany" 83)
         (list "France" 67)
         (list "Spain" 47))))

(define (empty-table columns) (table columns '()))

; Wstawianie

(define (type-of value)
  (cond [(string? value) 'string]
        [(number? value) 'number]
        [(boolean? value) 'boolean]
        [(symbol? value) 'symbol]
        [else (error "Unsupported value type")]))

(define (validate-row schema row)
  (unless (= (length schema) (length row))
    (error "Row has incorrect number of columns"))
  (for ([column-index (in-range (length schema))]
        [column (in-list schema)]
        [value (in-list row)])
    (unless (equal? (column-info-type column) (type-of value))
      (error "Incorect value type for column"))))

(define (table-insert row tab)
  (let ([schema (table-schema tab)]
        [rows (table-rows tab)])
    (validate-row schema row)
    (table schema (cons row rows))))

; Projekcja

(define (column-index column-name schema)
  (index-of (map column-info-name schema) column-name equal?))

(define (table-project cols tab)
  (let* ([old-schema (table-schema tab)]
         [old-rows (table-rows tab)]
         [new-schema (filter (lambda (column) (member (column-info-name column) cols)) old-schema)])
    (let ([new-rows (map (lambda (row)
                           (for/list ([column new-schema])
                             (let ([col-index (column-index (column-info-name column) old-schema)])
                               (list-ref row col-index))))
                         old-rows)])
      (table new-schema new-rows))))

; Sortowanie

(define (compare-values val1 val2)
  (cond
    [(and (string? val1) (string? val2))
     (string>? val1 val2)]
    [(and (number? val1) (number? val2))
     (> val1 val2)]
    [(and (boolean? val1) (boolean? val2))
     (and (not val1) val2)]
    [(and (symbol? val1) (symbol? val2))
     (string>? (symbol->string val1) (symbol->string val2))]))

(define (table-sort cols tab)
  (define (sort-helper rows cols)
    (if (null? cols)
        rows
        (let ([col-index (column-index (car cols) (table-schema tab))])
          (if col-index
              (sort-helper
               (sort rows
                     (lambda (row1 row2)
                       (let ([val1 (list-ref row1 col-index)]
                             [val2 (list-ref row2 col-index)])
                         (compare-values val1 val2))))
               (cdr cols))
              rows))))
  (table (table-schema tab) (reverse (sort-helper (table-rows tab) (reverse cols)))))

; Selekcja

(define-struct and-f (l r))             ; koniunkcja formuł
(define-struct or-f (l r))              ; dysjunkcja formuł
(define-struct not-f (e))               ; negacja formuły
(define-struct eq-f (name val))         ; wartość kolumny name równa val
(define-struct eq2-f (name name2))      ; wartości kolumn name i name2 równe
(define-struct lt-f (name val))         ; wartość kolumny name mniejsza niż val


(define (table-select form tab)
  (let* ([schema (table-schema tab)]
         [rows (table-rows tab)])
    (define (evaluate-formula form row)
      (cond
        [(eq-f? form)
         (equal? (list-ref row (index-of schema (findf (lambda (column) (equal? (column-info-name column) (eq-f-name form))) schema) equal?)) (eq-f-val form))]
        [(eq2-f? form)
         (let ([val1 (list-ref row (index-of schema (findf (lambda (column) (equal? (column-info-name column) (eq2-f-name form))) schema) equal?))]
               [val2 (list-ref row (index-of schema (findf (lambda (column) (equal? (column-info-name column) (eq2-f-name2 form))) schema) equal?))])
         (equal? val1 val2))]
        [(lt-f? form)
         (< (list-ref row (index-of schema (findf (lambda (column) (equal? (column-info-name column) (lt-f-name form))) schema) equal?)) (lt-f-val form))]
        [(and-f? form)
         (and (evaluate-formula (and-f-l form) row) (evaluate-formula (and-f-r form) row))]
        [(or-f? form)
         (or (evaluate-formula (or-f-l form) row) (evaluate-formula (or-f-r form) row))]
        [(not-f? form)
         (not (evaluate-formula (not-f-e form) row))]))
    (let ([selected-rows (filter (lambda (row) (evaluate-formula form row)) rows)])
      (table schema selected-rows))))

; Zmiana nazwy

(define (table-rename col ncol tab)
  (let* ([old-schema (table-schema tab)]
         [old-rows (table-rows tab)]
         [column-to-rename (findf (lambda (column) (equal? (column-info-name column) col)) old-schema)])
    (let ([new-schema (map (lambda (column)
                             (if (equal? (column-info-name column) col)
                                 (make-column-info ncol (column-info-type column))
                                 column))
                           old-schema)])
      (table new-schema old-rows))))

; Złączenie kartezjańskie

(define (table-cross-join tab1 tab2)
  (let* ([schema1 (table-schema tab1)]
         [schema2 (table-schema tab2)]
         [rows1 (table-rows tab1)]
         [rows2 (table-rows tab2)])
    (let ([combined-schema (append schema1 schema2)])
      (define (combine-rows row1 row2)
        (append row1 row2))
      (let ([joined-rows (for*/list ([row1 rows1] [row2 rows2])
                             (combine-rows row1 row2))])
        (table combined-schema joined-rows)))))

; Złączenie

(define (any? predicate lst)
  (ormap predicate lst))

(define (intersection lst1 lst2 predicate)
  (filter (lambda (x) (member x lst2 predicate)) lst1))

(define (table-natural-join tab1 tab2)
  (let* ([schema1 (table-schema tab1)]
         [schema2 (table-schema tab2)]
         [same-columns (intersection (map column-info-name schema1) (map column-info-name schema2) equal?)])

    (define renamed-tab2
      (foldl (lambda (column renamed-tab)
               (table-rename column (string-append (symbol->string column) "_renamed") renamed-tab))
             tab2
             same-columns))

    (define cross-joined (table-cross-join tab1 renamed-tab2))

     (define selected-rows	  	
       (foldl (lambda (column renamed-tab)	  	
                (table-select (eq2-f column (string-append (symbol->string column) "_renamed")) renamed-tab))	  	
              cross-joined	  	
              same-columns))

    (define projected-schema (remove-duplicates (append schema1 schema2) equal?))
    (define projected-columns (map column-info-name projected-schema))
    (table-project projected-columns selected-rows)))