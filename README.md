# CMPS 2200  Recitation 02

**Name (Team Member 1):**________Joshua Burch________ 
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

**TODO: your answer goes here**

  Case 1: f(n) = 1:
    W(n) = a*W(n/b)+1
    W(n) = O(n^log_(b)a)
  Case 2: f(n) = logn
    W(n) = a*W(n/b)+logn
    W(n) = O(n^(log_(b)a)logn)
  Case 3: f(n) = n
    W(n) = a*W(n/b)+n

  Results for f(n) = 1:
  W(10) = 15.00
  W(20) = 31.00
  W(50) = 63.00
  W(100) = 127.00
  W(200) = 255.00
  W(500) = 511.00
  W(1000) = 1023.00

  Results for f(n) = log n:
  W(10) = 8.29
  W(20) = 19.58
  W(50) = 52.20
  W(100) = 109.01
  W(200) = 223.31
  W(500) = 476.35
  W(1000) = 959.61

  Results for f(n) = n:
  W(10) = 36.00
  W(20) = 92.00
  W(50) = 276.00
  W(100) = 652.00
  W(200) = 1504.00
  W(500) = 4060.00
  W(1000) = 9120.00
    
Conclusion: Results match 
f(n) = 1, W(n) grows linearly
f(n) = logn, W(n) grows nlogn
f(n) = n, W(n) grows nlog_(b)a

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer.

**TODO: your answer goes here**

W(n) = a*W(n/b) + n^c

Case 1: c < log_(b)^a

  W(n) = O(n^log_(b)a)
  
  root dominated
  
Case 2: c > log_(b)a

  W(n) = O(n^c)
  
  leaf dominated
  
Case 3: c = log_(b)a

  W(n) = O((n^c)logn)
  
  balanced

Comparing work c < log_b(a)  and c=log_b(a)
|     n |           W_1 |    W_2 |
|-------|---------------|--------|
|    10 |        98.734 |     36 |
|    20 |       399.408 |     92 |
|    50 |      1706.669 |    276 |
|   100 |      6836.676 |    652 |
|  1000 |    443674.137 |   9120 |
|  5000 |  26036347.356 |  61728 |
| 10000 | 104145489.424 | 133456 |

 Comparing work c = log_b(a)  and c > log_b(a)
|     n |    W_1 |       W_2 |
|-------|--------|-----------|
|    10 |     36 |       174 |
|    20 |     92 |       748 |
|    50 |    276 |      4790 |
|   100 |    652 |     19580 |
|  1000 |   9120 |   1990744 |
|  5000 |  61728 |  49957880 |
| 10000 | 133456 | 199915760 

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**TODO: your answer goes here**
1. Give a formula and estimation
   Case 1: f(1)=1

   S(n)=S(n/2)+1

   O(logn)

   Case 2: f(n) = log(n)

   S(n)=S(n/2)+logn

   Case 3: f(n) = n

   S(n)=S(n/2)+n

   O(n)
   
3. Use code to verify that your estimations are correct
Comparing Span Functions:

Logarithmic vs. Log^2


|     n |   W_1 |    W_2 |
|-------|-------|--------|
|    10 |     4 |  5.605 |
|    20 |     5 |  8.601 |
|    50 |     6 | 13.506 |
|   100 |     7 | 18.111 |
|  1000 |    10 | 37.786 |
|  5000 |    13 | 56.944 |
| 10000 |    14 | 66.154 |

Comparing Span Functions: Log^2 vs. Linear
|     n |    W_1 |   W_2 |
|-------|--------|-------|
|    10 |  5.605 |    18 |
|    20 |  8.601 |    38 |
|    50 | 13.506 |    97 |
|   100 | 18.111 |   197 |
|  1000 | 37.786 |  1994 |
|  5000 | 56.944 |  9995 |
| 10000 | 66.154 | 19995 |
.
