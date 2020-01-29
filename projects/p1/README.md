# P1: Python practice 

**Assigned**: Week 1, January 28th, 2020

**Due**: Week 2, February 4th, 2020

**Late deadline**: Refer to syllabus for policy

## Description

You will be implementing some basic functions in Python as practice, including using iterators and built-in functions.

## Setup

Make sure Python 3.5+ is installed on your computer, and you should be good to go. We
won't be using virtual environments for this project, everything needed is built-in
with Python.

## Project

In `practice.py`, implement the following functions:

1. `hello_world()`

   Return the string `Hello, World!`

2. `sum_unique(l)`

   Given a list of integers, return the sum of the integers, not counting duplicates, i.e. 
   if you have two or more copies of an integer, it should be added to the final sum once.

   Examples:
   ```python
   >>> sum_unique([])
   0
   >>> sum_unique([4, 4, 5])
   9
   >>> sum_unique([4, 2, 5])
   11
   >>> sum_unique([2, 2, 2, 2, 1])
   3
   ```

3. `palindrome(x)`

    Given an integer or a string *x*, determine if *x* has the same value as *x* reversed.

    Examples:
    ```python
    >>> palindrome(1331)
    True
    >>> palindrome('racecar')
    True
    >>> palindrome(1234)
    False
    >>> palindrome('python')
    False
    ```

4. `sum_multiples(num)`

    Given a positive integer `num`, find the sum of all multiples of 3 and 5 upto and not including `num`.

    Examples:
    ```python
    >>> sum_multiples(10) # Multiples: [3, 5, 6, 9]
    23
    >>> sum_multiples(3) # Multiples: []
    0
    >>> sum_multiples(5) # Multiples: [3]
    3
    >>> sum_multiples(16) # Multiples: [3, 5, 6, 9, 10, 12, 15]
    60
    ```

5. `num_func_mapper(nums, funs)`

    Given a list of numbers `nums` and a list of functions `funs`, 
    apply each function to `nums` and store the result in a list.
    Return the list of results. 
    
    *Hint*: The list of results should be the same length as `funs`.

    Example:
    ```python
    >>> f_list = [sum_unique, sum]
    >>> num_list = [2, 2, 2, 4, 5]
    >>> all_the_sums(num_list, f_list)
    [11, 15]
    ```

6. `pythagorean_triples(n)`

    Finds all pythagorean triples where `a`, `b`, and `c` (side lengths of a triangle)
    are all less than `n` units long. This function should not return distinct tuples
    that still represent the same triangle. For example, (3, 4, 5) and (4, 3, 5)
    are both valid pythagorean triples, but **only the first** should be in the final list.

    The tuple elements should be sorted in ascending order, and the
    list of tuples should be sorted in ascending order by the last element of the tuple.

    Examples:
    ```python
    >>> pythagorean_triples(10)
    [(3, 4, 5)]
    >>> pythagorean_triples(11)
    [(3, 4, 5), (6, 8, 10)]
    >>> pythagorean_triples(20)
    [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17)]
    ```

## Testing

Navigate into the `p1/` directory and run the command `python3 tests.py` or the appropriate
command for your system. You should see your test results. If the printed report
says all tests were passed, then you can turn in your project.

## Submission & Grading

Submit `practice.py` to ELMS after testing thoroughly; all of your work should be in this module.
The ELMS page is not set up yet as of posting this project; it will be setup within a few days.

There are 12 public tests, and each will be worth 10 points.
