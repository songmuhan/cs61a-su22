(define (cadr lst) (car (cdr lst)))

(define (make-kwlist1 keys values)  (cons keys (list values)))

(define (get-keys-kwlist1 kwlist) (car kwlist))

(define (get-values-kwlist1 kwlist) (cadr kwlist))

(define (make-kwlist2 key values)
    (if (null? key)
        nil
        (cons (list (car key) (car values)) (make-kwlist2 (cdr key) (cdr values)))
    )
)

(define (get-keys-kwlist2 kwlist) 
    (if (null? kwlist)
        nil
        (cons (car (car kwlist)) (get-keys-kwlist2 (cdr kwlist)))
        )
)

(define (get-values-kwlist2 kwlist)
      (if (null? kwlist)
        nil
        (cons (cadr (car kwlist)) (get-values-kwlist2 (cdr kwlist)))
        )
)

(define (add-to-kwlist kwlist key value)
  (make-kwlist (append (get-keys-kwlist kwlist) (list key)) (append (get-values-kwlist kwlist) (list value)))
  )

(define (get-first-from-kwlist kwlist key)
(let (keys (get-keys-kwlist kwlist))
  (values (get-values-kwlist kwlist)))
 (cond ((null? keys) nil)
  ((= (car keys) key) (car values))
  (else get-first-from-kwlist (make-kwlist (cdr keys) (cdr values) ) key))
)

(define (get-first-from-kwlist kwlist key)
  (let ((keys (get-keys-kwlist kwlist)) (values (get-values-kwlist kwlist)))
  (cond ((null? keys) nil)
    ((equal? (car keys) key) (car values))
    (else (get-first-from-kwlist (make-kwlist (cdr keys) (cdr values)) key)))
  )
)