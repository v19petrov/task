class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def start(self):
        if self.speed > 0:
            print(f'{self.name} - go!')

    def stop(self):
        if self.speed == 0:
            print(f'{self.name} - stop!')

    def turn(self):
        turn = input('Where to turn? r/l: ')
        if turn == 'r':
            print(f'{self.name} turn in right')
        else:
            print(f'{self.name} turn in left')


c = Car(int(input('Enter speed: ')), 'green', 'Lincoln', 'is_police')
c.start()
c.stop()
c.turn()
class Towncar(Car):
    def on_speed(self, speed):
        if speed > 60:
            print(f'{self.name}, slow down!')

class Sportcar(Car):
    name = 'SportLincoln'

class Workcar(Car):
    def speed(self, speed):
        if speed > 40:
            print(f'{self.name}, slowly!')
class Policecar(Car):
    def police(self, speed):
        if speed > 160:
            print('it`s all right, we`ll catch up with them soon')
t = Towncar(60, 'yellow', 'Lada', 'is_police')
t.on_speed(170)