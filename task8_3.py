class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
    while True:
        in_data = []
        try:
            input_data = input('Введите положительное число, \nдля выхода нажмите /: ')
            if input_data == '/':
                break
            if not str(input_data).isdigit():
                OwnError = ValueError('Не число')
                raise OwnError
        except ValueError:
            print("Вы ввели не число")
        except OwnError as err:
            print(err)
        else:
            in_data.append(input_data)
            print(f"Все хорошо. Ваше число: {in_data} ")

