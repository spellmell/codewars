# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

"""
Your job is to write a function which increments a string,
to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to
the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be
considered.
"""
# import sys
# import re
# # from contextlib import suppress
#
#
# def increment_string(strng):
#     # with suppress(ValueError, TypeError):
#     s, num, tnum, ztnum = strng, 0, [], []
#     print(f"str_initial:{s}")
#
#     if not s:
#         return "1"
#     elif not s[-1].isdigit():
#         return s+str(1)
#     else:
#         if any(d.isdigit() for d in s):
#             [tnum.append(i) if i.isdigit() else tnum.append("_")
#              for i in s]
#             tnum = int(''.join(tnum).split("_")[-1])+1
#             num = ''.join(re.findall(r'\d', s))[len(str(tnum))*-1:]
#             print(f"num:{num}")
#             print(f"temp_num:{tnum}")
#             print(f"all_zeros:{all(True if z == '0' else False for z in s)}")
#             # string with zeros only
#             if all(True if z == "0" else False for z in s):
#                 print("all zero in s:True")
#                 ztnum = list(s.count("0")*"0")
#                 s = zreplace(ztnum)
#             # string with letters but only zeros in number
#             elif all(True if x == "0" else False for x in num):
#                 print("all zero in num:True")
#                 text = re.sub(r"\d", "", s)
#                 ztnum = list(s.count("0")*"0")
#                 s = text+str(zreplace(ztnum))
#             else:
#                 s = re.sub(str(num), str(tnum), s)
#
#     return s
#
#
# def zreplace(ztnum):
#     ztnum.pop(-1), ztnum.append("1")
#     ztnum = ''.join(ztnum)
#     print(f"ztnum_in_zreplace:{ztnum}")
#     return ztnum
#
#
# print(increment_string("foobar00"))
# print(sys.version)


import re


def increment_string(strng):
    s, num, tnum, ztnum = strng, 0, [], []
    if not s:
        return "1"
    elif not s[-1].isdigit():
        return s+str(1)
    else:
        if any(d.isdigit() for d in s):
            [tnum.append(i) if i.isdigit() else tnum.append("_")
             for i in s]
            tnum = int(''.join(tnum).split("_")[-1])+1
            num = ''.join(re.findall(r'\d', s))[len(str(tnum))*-1:]
            if all(True if z == "0" else False for z in s):
                ztnum = list(s.count("0")*"0")
                s = zreplace(ztnum)
            elif all(True if x == "0" else False for x in num):
                text = re.sub(r"\d", "", s)
                ztnum = list(s.count("0")*"0")
                s = text+str(zreplace(ztnum))
            else:
                s = re.sub(str(num), str(tnum), s)
    return s


def zreplace(ztnum):
    ztnum.pop(-1), ztnum.append("1")
    ztnum = ''.join(ztnum)
    return ztnum


print(increment_string("1945_foferoz:_10407080502030609"))
