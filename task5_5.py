import random


with open('task5_5.txt', 'w') as ran:
    my_sum = 0
    for i in range(50):
        lis = random.randint(1, 50)
        my_sum += lis
        ran.writelines(str(lis) + ' ')
    print('sum of numbers in the file:', my_sum)
