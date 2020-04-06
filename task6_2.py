
class Road:
    def __init__(self, lengt, width, thick, unit=25, ):
        self._lengt = lengt
        self._width = width

        print('Придется уложить', (lengt*width*thick*unit/1000), 'тонн асфальта')

r = Road(20, 5000, thick=int(input('Введите толщину асфальта: ')))
