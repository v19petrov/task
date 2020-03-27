def payroll():
    name = input('Имя сотрудника: ')
    rate_per_hour = int(input('Ставка в час: '))
    working_hours = int(input('Количество часов: '))
    prize = int(input('Премия: '))
    return (f'{name} получает {rate_per_hour*working_hours} печенек и премию {prize} печенек. Всего: {rate_per_hour*working_hours + prize} печенек')

