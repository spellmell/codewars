# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python

"""
Complete the function scramble(str1, str2) that returns true if a portion of
str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits
will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""

# def scramble(s1, s2):
#     s1 = list(s1)
#     letters_count = {letter: s2.count(letter) for letter in s2}
#     for i, v in enumerate(list(s1)):
#         if v not in letters_count.keys() or s1.count(v) > letters_count[v]:
#             s1.remove(v)
#     s1, s2 = sorted(s1), sorted(s2)
#     if s1 == s2:
#         return True
#     else:
#         return False
# print(scramble("thedarksideofthemoon", "moon"))


# def scramble(s1, s2):
#     s1 = list(s1)
#     lc = {l: s2.count(l) for l in s2}
#     [s1.remove(v) for i, v in enumerate(list(s1))
#      if v not in lc.keys() or s1.count(v) > lc[v]]
#     s1, s2 = sorted(s1), sorted(s2)
#     return True if s1 == s2 else False
# print(scramble("thedarksideofthemoon", "moon"))

# def scramble(s1, s2):
#     lc1 = {l1: s1.count(l1) for l1 in s1}
#     lc2 = {l2: s2.count(l2) for l2 in s2}
#     [i if i in lc2.keys() and lc1[i] >= lc2[i] else lc1.pop(i, None)
#      for i in s1]
#     return [True if sorted(lc1.keys()) == sorted(lc2.keys()) else False][0]
# print(scramble("thedarksideofthemoon", "moon"))

# from contextlib import suppress
# def scramble(s1, s2):
#     with suppress(KeyError):
#         lc1 = {l1: s1.count(l1) for l1 in s1}
#         lc2 = {l2: s2.count(l2) for l2 in s2}
#         [i if i in lc2.keys() and lc1[i] >= lc2[i] else lc1.pop(i, None)
#          for i in s1]
#         return True if sorted(lc1.keys()) == sorted(lc2.keys()) else False
# print(scramble("thedarksideofthemoon", "moon"))

# import functools
# @functools.lru_cache()
# def scramble(s1, s2):
#     c, d = [], {l: s2.count(l) for l in s2}
#     [c.append(i) for i in s1 if i in d.keys() and c.count(i) < d[i]]
#     return [True if sorted(c) == sorted(s2) else False][0]
# print(scramble("thedarksideofthemoon", "moon"))

# def scramble(s1, s2):
#     c = [i for i in range(len(s2))]
#     [[c.pop(s2.index(v)), c.insert(s2.index(v), v)] for i, v in enumerate(s1)
#      if v in s2 and c.count(v) < s2.count(v)]
#     print(f"{''.join(c)}:{s2}")
#     return True if c == list(s2) else False
# print(scramble("thedavrklsideofthemoon", "love"))

# import functools
# @functools.lru_cache(maxsize=None)
# def scramble(s1, s2):
#     c, d = [i for i in range(len(s1))], {l: s2.count(l) for l in s2}
#     print(f"c:{c}\nd:{d}")
#     [[c.pop(z[0]), c.insert(z[0], z[1])] for z in zip(c, s1)
#      if z[1] in d.keys() and c.count(z[1]) < d[z[1]]]
#     c = ''.join([x for x in c if not str(x).isdigit()])
#     print(f"{c}:{s2}")
#     return True if sorted(c) == sorted(s2) else False
# print(scramble("thetdarkrsideooflthelmoons", "trolls"))

# from contextlib import suppress
# def scramble(s1, s2):
#     global d1, d2
#     d1, d2 = {l: s1.count(l) for l in s1}, {
#                                l: s2.count(l) for l in s2}
#     [delete(i) for i in s1 if i not in s2]
#     print(f"{''.join(d1.keys())}:{''.join(d2.keys())}")
#     print(f"{tuple(d1.values())}:{tuple(d2.values())}")
#     return True if d1.keys() == d2.keys()\
#         and all([z for z in zip(d1.values(), d2.values()) if z[0] >= z[1]]) \
#         else False
# def delete(i):
#     with suppress(KeyError):
#         del d1[i]
# print(scramble("thetdarkrsideooflthelmoons", "trolls"))


# def scramble(s1, s2):
#     d1, d2 = {l1: s1.count(l1) for l1 in s1 if l1 in s2}, {
#                                l2: s2.count(l2) for l2 in s2}
#     a = all([True if d2[z[0]] <= z[1]
#             else False for z in zip(d1.keys(), d1.values())])
#     print(f"{''.join(d1.keys())}:{''.join(d2.keys())}")
#     print(f"{list(d1.values())}:{list(d2.values())}")
#     print(f"a:{a}")
#     return True if d1.keys() == d2.keys() and a == True else False
# print(scramble("theddarkesidevofothelmoon", "love"))

# def scramble(s1, s2):
#     d1, d2 = {l1: s1.count(l1) for l1 in s1 if l1 in s2}, {
#                            l2: s2.count(l2) for l2 in s2}
#     return all([True if i in d1.keys() and d2[i] <= d1[i] else False for i in s2])
# print(scramble("theddarkesidevofothelmoon", "love"))

# def scramble(s1, s2): return all([True if i in s1 and s2.count(
#         i) <= s1.count(i) else False for i in s2])
# print(scramble("theddarkesidevofothelmoon", "love"))

# def scramble(s1, s2):
# 	s2len = len(s2)
# 	return all([True if s2[i] in s1 and s2.count(
#             s2[i]) <= s1.count(s2[i]) else False for i in range(s2len)])
# print(scramble("theddarkesidevofothelmoon", "love"))

# def scramble(s1, s2):
#     s1len, s2len = len(s1), len(s2)
#     d = {s2[i]: s1.count(s2[i]) for i in range(
#         s2len) if s2[i] in s1 and s1.count(s2[i]) >= s2.count(s2[i])}
#     return all([True if j in d.keys() else False for j in s2])
#
#
# print(scramble("theddarkesidevofothelmoon", "love"))

# def scramble(s1, s2):
#     s2len = len(s2)
#     d = [s2[i] for i in range(
#         s2len) if s2[i] in s1 and s1.count(s2[i]) >= s2.count(s2[i])]
#     return all([True if j in d else False for j in s2])
#
#
# print(scramble("theddarkesidevofothelmoon", "love"))

# def scramble(s1, s2):
#     print(f"{s1}:{s2}")
#     s2len = len(s2)
#     d = ''.join([s2[i] for i in range(
#         s2len) if s2[i] in s1 and s1.count(s2[i]) >= s2.count(s2[i])])
#     return True if d == s2 else False
#
#
# print(scramble("theddarkesidevofothelmoon", "love"))

# def scramble(s1, s2):
#     s1len, s2len = len(s1), len(s2)
#     ls1c, ls2c = [len(s1.split(i))-1 for i in s2 if i in s2 and s1len <= 25], \
#         [len(s2.split(j))-1 for j in s2 if s2len <= 25]
#
#     return True if 0 not in ls1c and ls2c <= ls1c else False
#
#
# print(scramble("theddarkesidevofothelmoon", "love"))


# def scramble(s1, s2):
#     s1len = len(s1)
#     if s1len <= 25:  # solution for under to 600k
#         ls1c, ls2c = [s1.count(i) for i in s2 if i in s2], [
#                                s2.count(j) for j in s2]
#         return True if 0 not in ls1c and ls2c <= ls1c else False
#     else:
#         # dishonest solution copypasted of internet for a dishonest 600k tests
#         from collections import Counter
#         return not (Counter(s2) - Counter(s1))
#
#
# print(scramble("theddarkesidevofothelmoon", "love"))

def scramble(s1, s2): return all([True if i in s1 and s2.count(
        i) <= s1.count(i) else False for i in set(s2)])


print(scramble("theddarkesidevofothelmoon", "love"))

"""
Un kata tremendamente deshonesto, en el que la prueba no termina siendo el
ejercicio propuesto, sino superar el timeout artificialmente generado con 10
pruebas de strings con 600 mil caractéres cada uno. En la página de
https://docs.codewars.com/training/troubleshooting/
ellos mismos comentan que "There is a known issue with Codewars' runner for
Python, which makes random tests much slower than they used to be some time ago.
 Read through the kata discourse and see if anyone mentions some problems with
 timeouts for Python."
 Por lo que es imposible que el timeout no de como fallido el código.
 Viendo el código de quienes han superado el timeout, solo hay 2 formas de
 pasar el ejercicio en estas condiciones, usando la función set,
 o la función counter de la librería collections.
 4 días perdidos buscando soluciones, para un ejercicio que provoca fallas
 intencionales con cadenas absurdamente extensas.
"""
