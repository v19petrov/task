my_list = [el for el in range(1, 17, 2)]
print(my_list)
new_list = []
for i in range(1, len(my_list)):
    if int(my_list[i]) > int(my_list[i - 1]):
        new_list.append(my_list[i])
print(new_list)
