x = int(input('Enter number x: '))
y = int(input('Enter number y: '))
def my_func(a, b):
    res = a**b
    print(res)
my_func(x, y)


def div(c, d):
    return (1 if d == 0
            else div(c * c, d // 2) if d % 2 == 0
            else c * div(c, d - 1))

print(div(x, y))