i_dict = {"wage": 20000, "bonus": 30000}
class Worker:
    def __init__(self, name, surname, position):
        self.name = input('Enter name: ')
        self.surname = input('Enter surname: ')
        self.position = input('Enter you position: ')
        self._income = sum(i_dict.values())

    def arg(self, name, surname, position, income):
        print(self.name, self.surname, self.position, self._income)

class Position(Worker):
    def new(self, get_full_name, get_total_income):
        self.get_full_name = self.name + self.surname
        self.get_total_income = i_dict
        print(get_full_name)
        print(get_total_income)


w = Worker('name', 'surname', 'position',)
w.arg('name', 'surname', 'position', 'income')
