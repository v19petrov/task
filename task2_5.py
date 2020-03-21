my_list = [10,9,8,7,6,5,4,3,2,1]
print('Existing rating', (my_list))

user_n = int(input('Enter your number: '))
my_list.insert(0, user_n)

my_list.sort(reverse = True)
print(my_list)
print(f'Your ratihg at the moment: {my_list.index(user_n) + 2}')
