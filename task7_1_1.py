from copy import deepcopy


class Matrix:
    def __init__(self, a):
        self.a = deepcopy(a)

    def __str__(self):
        self.c = str(self.a)
        return self.c

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
        return Matrix(result)

m1 = Matrix([[1, 0, 3], [0, 1, 5], [8, 3, 1]])
m2 = Matrix([[0, 1, 0], [2, 0, 3], [1, 2, 0]])
print(m1 + m2)


