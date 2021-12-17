# https://www.codewars.com/kata/514b92a657cdc65150000006/python

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5
below the number passed in. Additionally, if the number is negative,
return 0 (for languages that do have them).
Note: If the number is a multiple of both 3 and 5, only count it once.
"""

mofl = [3, 5, 8, 11]


def check_multiples(below):
    multiples = []
    for i in range(2, below):
        for j in mofl:
            if i % j == 0 and i not in multiples:
                multiples.append(i)
    print(f"multiples of {mofl} up to {below}: {multiples}")
    return sum_list(multiples)


def sum_list(multiples):
    result = 0
    for r in multiples:
        result += r
    return result


print(f"the result of the sum of all multiples is: \
 {check_multiples(int(input('How much heigh do you want to fly? ')))}")
