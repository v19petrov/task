en_rus = {'one': 'один',
          'two': 'два',
          'three': 'три',
          'four': 'четыре'}
with open('task5_4_1.txt', 'a') as n_f:
    with open('task5_4.txt', 'r') as my_l:
        num = my_l.read().split('\n')
        for i in num:
            i = i.split(' - ')
            n_f.write(en_rus[i[0]] + ' - ' + i[1] + '\n')
print('I rewritten it')
