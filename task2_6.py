user_n = input('Enter the name of 3 products: ').split()
user_p = input('Enter the price of 3 products : ').split()
user_q = input('Enter the quantity of 3 products: ').split()
user_u = input('Enter the unit of measurement for 3 products: ').split()

my_goods1 = (1, {'name': user_n[0], 'price': user_p[0], 'quantity': user_q[0], 'u.of m.': user_u[0]})
my_goods2 = (2, {'name': user_n[1], 'price': user_p[1], 'quantity': user_q[1], 'u.of m.': user_u[1]})
my_goods3 = (3, {'name': user_n[2], 'price': user_p[2], 'quantity': user_q[2], 'u.of m.': user_u[2]})
print(my_goods1, my_goods2, my_goods3, sep=',\n')

my_dict = {'name:': user_n, 'price:': user_p, 'quant:': user_q, 'u. m.:': user_u}
for key, value in my_dict.items():
    print(key, value)
