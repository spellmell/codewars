
# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

"""
A format for expressing an ordered list of integers is to use a
comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated
from the end integer in the range by a dash, '-'.
The range includes all integers in the interval including both endpoints.
It is not considered a range unless it spans at least 3 numbers.
For example "12,13,15-17"
Complete the solution so that it takes a list of integers in
increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8,
         9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
"""


def solution(args):
    sl, el = [], []
    [sl.append(f"{args[i]}.") if len(sl) == 0 or args[i] == (args[i-1]+1)
     else [sl.append("_"), sl.append(f"{args[i]}.")] for i in range(len(args))]

    sl = ''.join(map(str, sl)).split("_")

    for j in sl:
        if j.count(".") < 3:
            tl = j.split(".")
            for k in tl:
                el.append(k)
        else:
            tl = j.split(".")
            el.append(f"{tl[0]}-{tl[-2]}")

    [el.pop(el.index(x)) for x in el if x == ""]
    return ','.join(el)


print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5,
      7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
