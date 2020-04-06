class Stationery:
    title = input('Enter title: ')
    def draw(self):
        print('Запуск отрисовки', self.title)

class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручки')

class Pensil(Stationery):
    def draw(self):
        print('Отрисовка карандаша')

class Hendle(Stationery):
    def draw(self):
        print('Отрисовка маркера')

s = Stationery()
s.draw()
p = Pen()
p.draw()
pn = Pensil()
pn.draw()
h = Hendle()
h.draw()