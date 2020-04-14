class ZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt
    a = input('Введите делимое: ')
    b = input('Введите делитель: ')
    try:
        a = int(a)
        b = int(b)
        if b == 0:
            raise ZeroDivisionError('На ноль не делится')
    except ValueError:
        print('Вы ввели не число')

    except ZeroDivisionError as err:
        print(err)

    else:
        print(f'Все хорошо, вот результат: {a/b}')
    finally:
        print('Мы закончили')

