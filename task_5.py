import  sys
receipt = int(input('Сумма выручка вашей компании за истекший период: '))
charge = int(input('Сумма издержек вашей компании за истекший период: '))

if receipt > charge:
    print('Ваша компания работает с прибылью')
elif receipt == charge:
    print('Вы в "нолях')
else:
    print('Ваша компания приносит убытки')
    print('Вы банкрот')
    sys.exit()

staff= int(input('Число сотрудников в штате вашей компании: '))

gein = receipt - charge
prof = gein * 100 / receipt
dividends = gein / staff
print('Рентабельность вашей компании составляет ', round(prof, 1),'процентов')
print('Дивиденды на каждого сотрудника: ', round(dividends, 1))


