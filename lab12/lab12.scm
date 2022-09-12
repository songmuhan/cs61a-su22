; Owner and Vehicle Abstraction
(define (make-owner name age)
  (cons name (cons age nil)))

(define (get-name owner) (car owner))

(define (get-age owner) (car (cdr owner)))

(define (make-vehicle model year previous-owners)
  (cons model (cons year previous-owners)))

(define (get-model vehicle) 'YOUR-CODE-HERE)

(define (get-year vehicle) 'YOUR-CODE-HERE)

(define (get-owners vehicle) 'YOUR-CODE-HERE)

(define (older-vehicle vehicle1 vehicle2)
  'YOUR-CODE-HERE)

(define (new-owner vehicle owner) 'YOUR-CODE-HERE)

(define (owners-names vehicle) 'YOUR-CODE-HERE)

(define (split-at lst n) 'YOUR-CODE-HERE)

; Tree Abstraction
; Constructs tree given label and list of branches
(define (tree label branches)
  (cons label branches))

; Returns the label of the tree
(define (label t) (car t))

; Returns the list of branches of the given tree
(define (branches t) (cdr t))

; Returns #t if t is a leaf, #f otherwise
(define (is-leaf t) (null? (branches t)))

(define (filter-odd t) 'YOUR-CODE-HERE)
