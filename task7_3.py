class Cell:
    def __init__(self, q1, q2):
        self.q1 = q1
        self.q2 = q2

    def __add__(self, other):
        return Cell(self.q1 + other.q1, self.q2 + other.q2)

    def __str__(self):
        return f'Новая клетка ({self.q1} , {self.q2})'

    def __sub__(self, other):
        n1 = self.q1 - other.q1
        n2 = self.q2 - other.q2
        if n1 < 0 or n2 < 0:
            return f'Нельзя вычитать большую клетку из меньшей'
        else:
            return f'Результат вычитания{self.q1 - other.q1, self.q2 - other.q2}'

    def __mul__(self, other):
        return Cell(self.q1 * other.q1, self.q2 * other.q2)

    def __truediv__(self, other):
        return Cell(int(self.q1 / other.q1), int(self.q2 / other.q2))

c1 = Cell(40, 20)
c2 = Cell(15, 30)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
