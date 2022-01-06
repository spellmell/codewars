# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""
from re import sub as s


def move_zeros(a):
    a, z = ''.join(str(a)), a.count(0)
    a = s(r"[^1-9]", "", a)+"0"*z
    return [int(i) for i in a]


print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
