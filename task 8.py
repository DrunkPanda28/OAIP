numbers = [1, 2, 8, 9, 4]

print(numbers)

#Удаляем один элемент по индексу
numbers.pop(2)
print(numbers)

#Срез
print(numbers[0:2])

#переворачиваем список 1 Способ
numbers = [1, 2, 8, 9]
numbers.reverse()
print(numbers)

#переворачиваем список 2 Способ
numbers = [1, 2, 8, 9]
reversed_numbers = numbers[::-1]
print(reversed_numbers)

#двумерный список
lst = [[j for j in range(1, 5)] for i in range(0, 2)]
print(lst)

#Очистка списка
print(numbers.clear())
