with open('task5_2_1.txt', 'r') as my_f:
    my_l = my_f.readlines()
    for index, value in enumerate(my_l):
        num = len(value.split())
        print('Number of words in line: {}'.format(num))
with open('task5_2_1.txt', 'r') as my_f:
    count = sum(1 for line in my_f)
    print('Number of lines in the file: {}'.format(count))
