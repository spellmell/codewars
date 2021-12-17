# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

"""
Write a function that takes in a string of one or more words,
and returns the same string, but with all five or more letter words reversed
(Just like the name of this Kata). Strings passed in will consist of only
letters and spaces. Spaces will be included only when more than one word
is present.
Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"
"""


def spin_words(sentence):
    string = []
    words = sentence.split()
    for i in words:
        if len(i) >= 5:
            word = ''.join(reversed(i))
        else:
            word = i
        string.append(word)
    return string


print(' '.join(spin_words(
    "Is not my fault I always run when the crocodile is incoming at home")))
