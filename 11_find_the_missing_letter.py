# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python
"""
#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
"""
import string


def find_missing_letter(chars):
    abc = list(string.ascii_lowercase+string.ascii_uppercase)
    chars_checker = abc[abc.index(chars[0]):abc.index(chars[0])+len(chars)]
    return [i for i in chars_checker if i not in chars][0]


print(find_missing_letter(['f', 'g', 'h', 'j', 'k']))
