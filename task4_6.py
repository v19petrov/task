from itertools import islice
from itertools import count
from itertools import cycle
lis_i = []
for i in islice(count(10), 11):
    lis_i.append(i)
print(lis_i)

q_list = [2, 4, 6, 8, 9, 11, 16, 35]
i_f = cycle(q_list)
for i in q_list:
    print(next(i_f))
