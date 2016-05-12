(define (propositions-in formula)
 (cond ((symbol? formula) (list formula))
       ((boolean? formula) '())
       ((and (list? formula) (not (null? formula)))
	(case (first formula)
	 ((not) (if (= (length formula) 2)
		    (propositions-in (second formula))
		    (panic "Unrecognized formula")))
	 ((and) (reduce unionq (map propositions-in (rest formula)) '()))
	 ((or) (reduce unionq (map propositions-in (rest formula)) '()))
	 (else (panic "Unrecognized formula"))))
       (else (panic "Unrecognized formula"))))

(define (all-truth-assignments propositions)
 (if (null? propositions)
     '(())
     (let ((truth-assignments (all-truth-assignments (rest propositions))))
      (append (map (lambda (truth-assignment)
		    (cons (list (first propositions) #t) truth-assignment))
		   truth-assignments)
	      (map (lambda (truth-assignment)
		    (cons (list (first propositions) #f) truth-assignment))
		   truth-assignments)))))

(define (lookup-proposition proposition truth-assignment)
 (cond ((null? truth-assignment) (panic "Proposition not in truth assignment"))
       ((eq? proposition (first (first truth-assignment)))
	(second (first truth-assignment)))
       (else (lookup-proposition proposition (rest truth-assignment)))))

(define (boolean-evaluate formula truth-assignment)
 (cond ((symbol? formula) (lookup-proposition formula truth-assignment))
       ((boolean? formula) formula)
       ((and (list? formula) (not (null? formula)))
	(case (first formula)
	 ((not) (if (= (length formula) 2)
		    (not (boolean-evaluate (second formula) truth-assignment))
		    (panic "Unrecognized formula")))
	 ((and) (every (lambda (formula)
			(boolean-evaluate formula truth-assignment))
		       (rest formula)))
	 ((or) (some (lambda (formula)
		      (boolean-evaluate formula truth-assignment))
		     (rest formula)))
	 (else (panic "Unrecognized formula"))))
       (else (panic "Unrecognized formula"))))

(define (truth-table formula)
 (map (lambda (truth-assignment)
       (list truth-assignment (boolean-evaluate formula truth-assignment)))
      (all-truth-assignments (propositions-in formula))))
   
   
 

  

  
  

      

  




	
	