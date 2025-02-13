from main import *


def test_simple_work():
	assert simple_work_calc(10, 2, 2) == 36  #TODO
	assert simple_work_calc(20, 3, 2) == 230  #TODO
	assert simple_work_calc(30, 4, 2) == 650  #TODO
	
	#Additional 3 Cases
	assert simple_work_calc(40, 2, 2) == 224
	assert simple_work_calc(50, 2, 2) == 276
	assert simple_work_calc(60, 3, 2) == 960


def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 15  #TODO
	assert work_calc(20, 1, 2, lambda n: n * n) == 530  #TODO
	assert work_calc(30, 3, 2, lambda n: n) == 300  #TODO
	
	#Additional 3 Cases
	assert work_calc(40, 2, 2, lambda n: n) == 224
	assert work_calc(50, 2, 2, lambda n: n) == 276
	assert work_calc(60, 3, 2, lambda n: n) == 960


def test_compare_work():
	
	sizes = [10, 20, 50, 100, 1000, 5000, 10000]

	#changing original code for Question 5 c < log_b a
	work_fn1 = lambda n: work_calc(n, 4, 2, lambda n: n**0.5)
	
	#changing original code for Question 5 c > log_b a
	work_fn2 = lambda n: work_calc(n, 2, 2, lambda n: n)

	#changing original code for Question 5 c = log_b a
	work_fn3 = lambda n: work_calc(n, 2, 2, lambda n: n**2)
	
	comparison1 = compare_work(work_fn1, work_fn2, sizes)
	comparison2 = compare_work(work_fn2, work_fn3, sizes)
	#Quetion 5 Empirical Results Printed:
	print("\nComparing Work Functions: c < log_b a vs. c = log_b a")
	print_results(comparison1)

	print("\nComparing Work Functions: c = log_b a vs. c > log_b a")
	print_results(comparison2)

	assert comparison1 is not None
	assert comparison2 is not None


def test_compare_span():
	# TODO

	sizes = [10, 20, 50, 100, 1000, 5000, 10000]
	
	# Span for f(n) = 1 (Log Span)
	span_fn1 = lambda n: span_calc(n, 2, 2, lambda n: 1)

	# Span for f(n) = log(n) (Log^2 Span)
	span_fn2 = lambda n: span_calc(n, 2, 2, lambda n: math.log(n))

	# Span for f(n) = n (Linear Span)
	span_fn3 = lambda n: span_calc(n, 2, 2, lambda n: n)

	comparison1 = compare_span(span_fn1, span_fn2, sizes)
	comparison2 = compare_span(span_fn2, span_fn3, sizes)

	#Question 6 Empirical Results Printed:
	print("\nComparing Span Functions: Logarithmic vs. Log^2")
	print_results(comparison1)

	print("\nComparing Span Functions: Log^2 vs. Linear")
	print_results(comparison2)

	assert comparison1 is not None
	assert comparison2 is not None