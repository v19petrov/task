
def my_division():
    an_1 = int(input('Enter first number: '))
    an_2 = int(input('Enter second number: '))
    try:
        an_1 / an_2
    except ZeroDivisionError:
        print('Stupid man! You can`t divide by zero')
        an_1 = int(input('Enter first number: '))
        an_2 = int(input('Enter second number: '))
    return round(an_1 / an_2, 2)

print(f"If you divide them you can: {my_division()}")

