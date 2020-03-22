## Polynomials and Derivates

# Task

*Taken from the course's github*

Using your OO knowledge, implement a program that takes a string, 
representing a polynomial function and returns / prints 
the derivative of that polynomial function.

Example:

```
$ python3 solution.py '2*x^3+x'
Derivative of f(x) = 2*x^3 + x is:
f'(x) = 6*x^2 + 1
```
# About the task

We assume that the input is correct. 

We assume that only addition is allowed between terms.

We assume that there won't be terms that look like:

* x^3^3
* x^x^5
* x^x

*Important:* 

The static validation functions are there for the purpose of 
practicing to write unit tests. They do **NOT** handle every possible input.

# Solution

The classes 'Term' and 'Polynomial' are inside the **polynomial.py** file.
They are taking care of the representation of the whole expression.

The **utils.py** file is where the parser, the function that validates the 
terminal call and the term splitter are. 

The **solution.py** is used to create the connection between the other
two.

The files which names start with *tests_* contain some unit tests respectively 
for **polynomial.py** and **utils.py**