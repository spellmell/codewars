# https://www.codewars.com/kata/51e056fe544cf36c410000fb/python
"""
Write a function that, given a string of text (possibly with punctuation and
line-breaks), returns an array of the top-3 most occurring words,
in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more
apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word
('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should
be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be
lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or
top-1 words should be returned, or an empty array if a text contains no words.
Examples:
top_3_words("In a village of La Mancha, the name of which I have no desire
to call to mind, there lived not long since one of those gentlemen that
keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound
for coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]
Bonus points (not really, but just for fun):
Avoid creating an array whose memory footprint is roughly as big as the input
text.
Avoid sorting the entire array of unique words.
"""

# from re import sub as s
#
#
# def top_3_words(text):
#     print(f"TEXT: {text}\n")
#
#     words, mow = [], []
#
#     words = text.split(" ")
#     words = [s(r"[^a-zA-Z]+", "", i).lower()
#              if len(set(i)) <= 2 else s(r"[.:,;¡¿?!/$%&()_-]", " ", i).lower()
#              for i in words]
#     words = ' '.join(words).split(" ")
#
#     print(f"WORDS: {words} {len(set(words))}\n")
#
#     dict = {word: words.count(word) for word in words if word != ''}
#     print(f"DICT: {dict} {len(dict)}\n")
#
#     #  most occurring words
#     mow = list(reversed(sorted([x for x in zip(dict.values(), dict.keys())])))
#     print(f"MOW: {mow}\n")
#
#     output = [t[1] for t in mow][:3]
#     print(f"{output}\n")
#     return output
#
#
# # print(top_3_words("In a village of La Mancha, the name of which I have no \
# # desire to call to mind, there lived not long since one of those gentlemen that \
# # keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound \
# # for coursing. An olla of rather more beef than mutton, a salad on most \
# # nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra \
# # on Sundays, made away with three-quarters of his income."))
# print(top_3_words("  //wont won't won't "), ["won't", "wont"])

from re import sub as s


def top_3_words(text):
    words, mow = [], []
    words = text.split(" ")
    words = [s(r"[^a-zA-Z]+", "", i).lower()
             if len(set(i)) <= 2 else s(r"[.:,;¡¿?!/$%&()_-]", " ", i).lower()
             for i in words]
    words = ' '.join(words).split(" ")
    dict = {word: words.count(word) for word in words if word != ''}
    mow = list(reversed(sorted([x for x in zip(dict.values(), dict.keys())])))
    output = [t[1] for t in mow][:3]
    return output


print(top_3_words("In a village of La Mancha, the name of which I have no \
desire to call to mind, there lived not long since one of those gentlemen that \
keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound \
for coursing. An olla of rather more beef than mutton, a salad on most \
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra \
on Sundays, made away with three-quarters of his income."))
