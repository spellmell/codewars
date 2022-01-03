# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

"""
Your task in order to complete this Kata is to write a function which formats
a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just
returns "now". Otherwise, the duration is expressed as a combination of
years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc.
In general, a positive integer and one of the valid units of time, separated
by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", ").
Except the last component, which is separated by " and ",
just like it would be written in English.

A more significant units of time will occur before than a least significant
one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not
repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence,
1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the
function should not return 61 seconds, but 1 minute and 1 second instead.
Formally, the duration specified by of a component must not be greater than
any valid more significant unit of time.
"""

# from re import sub as s
# from random import randint as r
#
# t = 0
#
#
# def rest(time, fct):
#     # calculating the remaining time
#     global t
#     r, t = time // fct, time % fct
#     return r
#
#
# def format_duration(seconds):
#     if not seconds:
#         return "now"
#     else:
#         global t
#         t, output = seconds, []
#
#         l, f, r = ["years", "days", "hours", "minutes", "seconds"], \
#             {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400,
#              'years': 31536000}, []
#
#         # list creation with time values
#         r = [rest(t, f[i]) if t >= f[i] else print("") for i in l]
#         # matching values with labels
#         o = s(r"[(,)\[\]']", "",
#               str([j for j in zip(r, l) if j[0] != None])).split(" ")
#
#         for k, h in enumerate(o):
#             # separators
#             if len(o) > 2 and h != o[-3]:
#                 sep = ", "
#             else:
#                 sep = " and "
#             if k % 2 == 0:
#                 output.append(f"{h} ")  # nums
#             else:  # time labels
#                 # insertion separators and cut in only 1
#                 if int(o[k-1]) == 1:  # if number is > 1
#                     if h != o[-1]:
#                         output.append(f"{''.join(list(h)[:-1])}{sep}")
#                     else:
#                         output.append(f"{''.join(list(h)[:-1])}")
#                 else:
#                     if h != o[-1]:
#                         output.append(f"{h}{sep}")
#                     else:
#                         output.append(f"{h}")
#
#     output = ''.join(output)
#
#     return output
#
#
# # print(format_duration(r(0, 6000000000)))
# print(format_duration(3662))

from re import sub as s
from random import randint as r

t = 0


def rest(time, fct):
    # calculating the remaining time
    global t
    r, t = time // fct, time % fct
    return r


def format_duration(seconds):
    if not seconds:
        return "now"
    else:
        global t
        t, output = seconds, []

        l, f, r = ["years", "days", "hours", "minutes", "seconds"], \
            {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400,
             'years': 31536000}, []

        # creation list with time values
        r = [rest(t, f[i]) if t >= f[i] else print("") for i in l]
        # matching values with labels
        o = s(r"[(,)\[\]']", "",
              str([j for j in zip(r, l) if j[0] != None])).split(" ")

        for k, h in enumerate(o):
            # separators
            if len(o) > 2 and h != o[-3]:
                sep = ", "
            else:
                sep = " and "
            if k % 2 == 0:
                output.append(f"{h} ")  # nums
            else:  # time labels
                # insertion separators and cut in only 1
                if int(o[k-1]) == 1:  # if number is > 1
                    if h != o[-1]:
                        output.append(f"{''.join(list(h)[:-1])}{sep}")
                    else:
                        output.append(f"{''.join(list(h)[:-1])}")
                else:
                    if h != o[-1]:
                        output.append(f"{h}{sep}")
                    else:
                        output.append(f"{h}")

    output = ''.join(output)

    return output


print(format_duration(r(0, 6000000000)))
