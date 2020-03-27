from math import factorial

num = [el for el in range(10, 50)]


def gen():
    for i in num:
        j = str(i * factorial(i - 1))
        s = (j[0:15] if len(j) > 15 else j)
        yield s


for i in gen():
    print(i)
