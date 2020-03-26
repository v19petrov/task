user_name = input('Enter your name: ')
user_surname = input('Enter your surname: ')
user_birth = input('Enter your year of birth: ')
user_city = input('What city are you in: ')
user_email = input('Enter your email: ')
user_phone = input('Enter your phone number: ')

def c_data(name, surname, birth, city, email, phone):
    print(f' client {name} {surname}, {birth} year of birth, located in the city {city}, email: {email}, phone: {phone}')

c_data(name=user_name, surname=user_surname, birth=user_birth, city=user_city, email=user_email, phone=user_phone)