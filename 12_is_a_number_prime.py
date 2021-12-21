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

# my first attempt:
# import random as rnd#
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
# print(f"\n{is_prime(rnd.randint(0,666))}")

# my first attempt 2:
# method: eratosthenes sieve
# functional but does not pass the efficiency in attempt for very high numbers:
# "Execution Timed Out (12000 ms)"
# 2000000000 qhdp!
#
# from random import randint as rnd
# def is_prime(num):
#     m = [i for i in range(2, num+1)]
#     [[m.remove(k) for k in m if k % j == 0 and k != j]
#      for j in m if j ** 2 <= num]
#     print(num)
#     return True if num in m else False
# print(is_prime(rnd(0, 666)))

# my second attempt:
# is also inefficient in the attempt:
# from random import randint as rnd
# def is_prime(num): return [False if num <= 1 or num > 2 and num % 2 == 0 else all(
#             num % i for i in range(2, num))][0]
# rndn = rnd(0, 666)
# print(f"Is {rndn} prime? {is_prime(rndn)}")

# https://docs.codewars.com/training/troubleshooting/
# "There is a known issue with Codewars' runner for Python, which makes random
# tests much slower than they used to be some time ago. Read through the kata
# discourse and see if anyone mentions some problems with timeouts for Python."

# from math import factorial as f
# def is_prime(num): return f(num-1) % num == num - 1
# print(is_prime(153))

# http://montreal.pm.org/tech/neil_kandalgaonkar.shtml
# import re
# def is_prime(n): return not re.match(r'^1?$|^(11+?)\1+$', n*'1')
# print(is_prime(153))


from random import randint as rnd
from math import sqrt as q


def is_prime(num):
    print(num)
    return [False if num <= 1 or num > 2 and num % 2 == 0 else all(
            num % i for i in range(2, round(q(num)+1)))][0]


print(is_prime(rnd(0, 153)))
