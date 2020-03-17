time = int(input('Введите время в секундах: '))
minutes = (time // 60) % 60
hours = time // 3600
seconds = time % 60
if minutes < 10:
    minutes = str('0' + str(minutes))
else:
    minutes = str(minutes)
if seconds < 10:
    seconds = str ('0' + str(seconds))
else:
    seconds = str(seconds)

print('У вас осталось времени: ',hours,':',minutes,':',seconds)


