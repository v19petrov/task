import random
class Matrix:
    def __init__(self):
        self.a = [[random.randint(0, 9) for i in range(0, 3)] for j in range(0, 3)]
        print(self.a)

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                s = other.a[i][j] + self.a[i][j]
                numbers.append(s)
                if len(numbers) == len(self.a):
                    result.append(numbers)
                    numbers = []
        return result

    def __str__(self):
        self.c = str(self.a)
        return self.c

m1 = Matrix()
m2 = Matrix()
print(m1 + m2)


