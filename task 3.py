a = int(input("Введите сумму: \n"))
digits_of_number = []

#print(a % 10)  показывает первый разряд числа
#print(a // 10) удаляет последний разряд числа

for i in range(3):
    b = a % 10
    a = a // 10
    digits_of_number.append(b)

digits_of_number.append(a)

print(str(digits_of_number[0]), " - 1р")
print(str(digits_of_number[1]), " - 10р")
print(str(digits_of_number[2]), " - 100р")
print(str(digits_of_number[3]), " - 1000р")
