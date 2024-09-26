salary = int(input('Зарплата за месяц: '))
working_hours = int(input("Количество отработанных в выходные часов: "))
award = salary * 0.01 * working_hours

print("Размер премии:", award)
