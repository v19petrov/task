
with open('m_enter.txt', 'w') as m_f:
    while True:
        my_t = (input('Enter the desired text\n to finish click "Enter": '))
        if not my_t:
            break
        m_f.write(my_t + '\n')




