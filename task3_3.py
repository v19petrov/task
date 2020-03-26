user_a = int(input('Enter number 1: '))
user_b = int(input('Enter number 2: '))
user_c = int(input('Enter number 3: '))

def my_f(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    my_list.reverse()
    your_list = my_list.pop(-1)
    print(f'The smallest value is {your_list} and the sum of the remaining values {sum(my_list)}')

my_f(user_a, user_b, user_c)





