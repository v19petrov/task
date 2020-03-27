from functools import reduce

m_list = [el for el in range(100, 1002, 2)]
print(m_list)
print(reduce((lambda a, b: a*b), m_list))
