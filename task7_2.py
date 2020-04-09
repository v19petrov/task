

class Cloth:

    def my_met1(self, num1, num2):
        self.num1 = int(input('Введите неободимое количество пальто: '))
        self.num2 = int(input('Введите неободимое количество костюмов: '))


class Coat(Cloth):

    def my_met2(self, num1, summ, v):
        self.v = int(input('Задайте размер пальто '))
        self.num1 = int(input('Введите неободимое количество пальто: '))
        self.summ = num1*v/6.5 + 0.5
        return f'Для создания {num1} изделий необходимо {summ} м ткани'


class Suit(Cloth):

    def my_met2(self, num1, summ, v):
        self.v = v
        self.num1 = int(input('Введите неободимое количество костюмов: '))
        self.summ = num1 * v / 6.5 + 0.5
        return f'Для создания {num1} изделий необходимо {summ} м ткани'


s1 = Coat()
s2 = Suit()
print(s1.my_met2('num1', 'summ', 'v'))