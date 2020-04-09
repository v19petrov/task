
class Matrix:
    def __init__(self, a):
        self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in a])
        mist = []
        for i in a:
            mist.append([j for j in i])
        self.a = mist

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

    def __str__(self):
        self.c = str(self.a)
        return self.c

m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 4, 9], [1, 2, 0]])
print(m1 + m2)

