import json
import math

with open('task5_7_2.json', 'w', encoding='utf-8') as sit:
    with open('task5_7_1.txt') as cat:
        result = []
        name = {}
        for line in cat:
            name[line.split()[0]] = int(line.split()[2]) - int(line.split()[3])
        res = sum([int(i) for i in name.values() if int(i) > 0]) / len([int(i) for i in name.values() if int(i) > 0])
        result.append(name)
        for key, value in name.items():
            print(key, ': ', value, sep='')
    json.dump(result, sit)
    json.dump(math.ceil(res), sit)