class Cloth:
    def __init__(self):
        self.coat = int(input('Сколько нужно пальто: '))
        self.suit = int(input('Сколько нужно костюмов: '))

    @property
    def on_data(self):
        self.v = int(input('Введите размер для пальто: ')) * self.coat / 6.5 + 0.5
        self.h = int(input('Введите рост для костюма: ')) * self.suit * 2 + 0.3
        return f'На {self.coat} пальто необходимо {self.v.__round__(2)} м ткани, на {self.suit} костюмов - {self.h.__round__(2)} м ткани,\nВсего нужно {(self.v + self.h).__round__(2)} м ткани'


c = Cloth()
print(c.on_data)
