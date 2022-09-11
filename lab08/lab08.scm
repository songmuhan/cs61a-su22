(define (over-or-under num1 num2) (cond ((> num1 num2) 1) ((= num1 num2) 0) (else -1)))

(define (composed f g) (lambda (x) (f (g x))))

(define (square n) (* n n))

(define (pow base exp)(if (= exp 1) base ( if (even? exp) (square (pow base (/ exp 2)))(* base (square (pow base (/ (- exp 1) 2)))))))

(define (ascending? lst) (if (null?(cdr lst)) #t (if (>  (car lst) (car (cdr lst))) #f (ascending? (cdr lst)))))