
user_m = int(input('Enter the month number:  '))
m_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2]
# while True:
#     if user_m <= 0 or user_m > 12:
#         user_m = int(input('Enter the month number from 1 to 12: '))
#     else:
#         break
if user_m in m_list[:3]:
    print('You`re in spring')
elif user_m in m_list[3:6]:
    print('You`re in summer')
elif user_m in m_list[6:9]:
    print('You`re in autumn')
elif user_m in m_list[9:]:
    print('You`re in winter')

my_dict = {'spring': [3, 4, 5],  'summer': [6, 7, 8], 'autumn': [9, 10, 11], 'winter': [1, 2, 12]}
for season, months in my_dict.items():
    if user_m in months:
        print(season)
