number = int(input('Ведите число: '))
if number >= 100:
    number = int(input('Введите двузначное число: '))
if number < 0:
    number = int(input('Введите положительное двузначное число: '))
number_2 = number*11
number_3 = number*111

print((str(number) + '+' + str(number_2) + '+' + str(number_3)), '=', (number + number_2 + number_3))