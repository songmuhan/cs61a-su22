(define (tail-replicate x n)
    (define (helper counter lst)
       (if (= counter 0) 
            lst
           (helper (- counter 1) (cons x lst)) )
    )
    (helper n nil)
)
