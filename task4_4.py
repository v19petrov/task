from functools import reduce

f_list = [7, True, 5, 7, 5, 3, 8, 9, 7, 'oneonline', 2, 1, True, 8, 3, 2, 1, 7, 9]
# option 1
def uf_list(f):
    un_list = []
    for i in f:
        if i not in un_list:
            un_list.append(i)
    print(un_list)

uf_list(f_list)

# option 2
origin_list = reduce(lambda i, x: i.append(x) or i if x not in i else i, f_list, [])
print(origin_list)