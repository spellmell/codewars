# https://www.codewars.com/kata/55b42574ff091733d900002f/train/python

"""
Make a program that filters a list of strings and returns a list with only
your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a
friend of yours! Otherwise, you can be sure he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.
friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
"""


def friend(x):
    my_friends = []
    for f in x:
        if len(f) == 4:
            my_friends.append(f)
    return my_friends


print(friend(['Pedro', 'Marta', 'Kora', 'Nako',
      'Victoria', 'Sofia', 'Ana', 'Raul', 'Gimena']))
