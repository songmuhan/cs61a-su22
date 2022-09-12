(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (interleave lst1 lst2)
    (cond ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (cons (car lst1) (interleave lst2 (cdr lst1)))))
)

(define (my-filter pred lst) 
    (cond ((null? lst) nil)
        ((pred (car lst)) (cons (car lst) (my-filter pred (cdr lst))))
        (else (my-filter pred (cdr lst)))
        )
    
)


(define (concatenate s) 
 (if (null? s)
    nil
    (append (car s) (concatenate (cdr s)))
    )
)

