import calendar

print('добро пожаловать в календарь\n')

year = int(input('Пожалуйста введите год: '))
month = int(input('Введите номер любимого месяца: '))

print(calendar.month(year,month))

print('Всего хорошего')