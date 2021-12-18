# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

"""
Complete the solution so that it splits the string into pairs of two characters
If the string contains an odd number of characters then it should replace the
missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""


def solution(s):
    pairs = []
    for i in range(0, len(s), 2):
        cut = s[i:i+2]
        if len(cut) < 2:
            cut += "_"
        pairs.append(cut)
    return pairs


print(solution("_codewars.com"))
