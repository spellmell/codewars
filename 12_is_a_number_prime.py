# https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python
"""
Define a function that takes one integer argument and returns logical value
true or false depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1
that has no positive divisors other than 1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive.
You may be given negative numbers as well (or 0).
NOTE on performance: There are no fancy optimizations required,
but still the most trivial solutions might time out. Numbers go up to 2^31
(or similar, depends on language version). Looping all the way up to n,
or n/2, will be too slow.

Example

is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */

"""

# import random as rnd
#
# matrix = []
#
#
# def is_prime(num):
#     matrix = [i for i in range(2, num+1)]
#     print(f"{num}\n\n{matrix}\n\n")
#     for j in matrix:
#         if j ** 2 <= num:
#             for k in matrix:
#                 if k % j == 0 and k != j:
#                	    matrix.remove(k)
#                	    print(k)
#
#     print(f"{num}\n\n{matrix}\n\n{num}")
#
#     if num in matrix:
#         return True
#     else:
#         return False
#
#
# print(f"\n{is_prime(rnd.randint(0,666))}")


import random as rnd


def is_prime(n):
    m = [i for i in range(2, n+1)]
    [[m.remove(k) for k in m if k % j == 0 and k != j]
     for j in m if j ** 2 <= n]
    return True if n in m else False


print(is_prime(rnd.randint(0, 666)))
