import re

with open('task5_6_1.txt', 'r', encoding='utf-8') as uni:
    for line in uni.readlines():
        my_s = sum(map(int, re.findall(r'\d+', line)))
        if line.islower():
            print(line, my_s)
