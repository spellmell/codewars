# https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python

"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in
Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!!
"""


def expanded_form(num):
    lnum = list(str(num))
    lenl = len(lnum)
    for i in lnum:
        index = lnum.index(i)
        if int(lnum[index]):
            lnum[index] = lnum[index] + \
                            "0"*(len(lnum[index:])-1)

    while lnum.count("0") > 0:
    	for k in lnum:
            if k == "0":
            	lnum.pop(lnum.index(k))

    output = ' + '.join(list(lnum))
    return output


print(expanded_form(int(input("ingresa un número entero:"))))
