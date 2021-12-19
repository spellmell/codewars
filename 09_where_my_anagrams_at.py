# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python

"""
What is an anagram? Well, two words are anagrams of each other if they both
contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words.
You should return an array of all the anagrams or an empty array if there
are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer',
'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""

# def anagrams(word, words):
#     letters_counter = {}
#     for letter in word:
#         letters_counter[letter] = word.count(letter)
#     words_ok = []
#     for i in words:
#         if len(i) == len(word):
#             for j in i:
#                 try:
#                     if i.count(j) == letters_counter[j] and sorted(i) == \
#                             sorted(word) and i not in words_ok:
#                         words_ok.append(i)
#                 except KeyError:
#                     pass
#     print(f"letters_counter: {letters_counter}\n")
#     return words_ok
#
#
# print(anagrams("baraka", ["rakbea", "akbaras",
#       "akarab", "krasbar", "brakaa", "bkaara"]))

# -------------------------------------------------------------------


def anagrams(word, words):
    letters_count = {letter: word.count(letter) for letter in word}
    words_ok = []
    [list(words_ok.append(i) for j in i if j in letters_count.keys()
          and i.count(j) == letters_count[j] and sorted(i) == sorted(word)
          and i not in words_ok) for i in words
     if len(i) == len(word)]
    return words_ok


print(anagrams("bersa", ["besar", "asrob",
                         "akarab", "rebas", "brakaa", "sareb"]))

# print(anagrams("sado", ["odas", "daso",
#                         "akarab", "odsa", "brakaa", "sareb"]))

# print(anagrams("baraka", ["rakbea", "akbaras",
#       "akarab", "krasbar", "brakaa", "bkaara"]))
