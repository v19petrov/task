user_number = int(input('Введите многозначное число: '))

max_number = user_number%10
user_number = user_number//10

while user_number > 0:
   if user_number%10 > max_number:
       max_number = user_number%10
   user_number = user_number//10

print('Самая большая цифра:', max_number)


