class myError(Exception):
    def __init__(self, user_n, user_q, user_p):
        self.user_n = user_n
        self.user_q = user_q
        self.user_p = user_p

    def ent(self):
        try:
            self.user_n = input('Введите наименование: ')
            self.user_q = input('Ведите количество: ')
            self.user_p = input('Введите цену: ')
            if not str(self.user_q).isdigit():
                myError = ValueError('Вы ввели не число')
                raise myError
        except ValueError as err:
            print(err)
        else:
            return self.user_n, self.user_q, self.user_p



class Off_eq:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        print('==================================')
        print(f'{self.name} | количество: {self.quantity} | цена: {self.price}')


class Printer(Off_eq):
    def __init__(self, name, model, quantity, price):
        super().__init__(name, quantity, price)
        self.model = model
        print(self.model)


class Scanner(Off_eq):
    def __init__(self, name, model, quantity, price):
        super().__init__(name, quantity, price)
        self.model = model
        print(model)


class Xerox(Off_eq):
    def __init__(self, name, color, quantity, price):
        super().__init__(name, quantity, price)
        self.color = color
        print(self.color)


r1 = Off_eq('Xerox', 6, 23500)
r2 = Off_eq('Printer', 2, 12000)
r3 = Off_eq('Scanner', 3, 8000)
x1 = Xerox('Xerox', 'no color', 6, 23500)
s1 = Scanner('Scanner', "Panas", 3, 8000)
p1 = Printer('Printer', "Sionio", 2, 12000)
e = myError('user_n', 'user_q', 'user_p')
print(e.ent())
