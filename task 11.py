#Создание пустого словаря
empty_dict = {}
print(empty_dict)

#Создание словаря с элементами
my_dict = {"имя": "Иван",
           "фамилия": "Павлов",
           "возраст": 21}

print(my_dict)

# Добавляем новое значение
my_dict["профессия"] = "инженер"

print(my_dict)

# Удаляем ключ "возраст"
del my_dict["возраст"]

print(my_dict)

my_dict["фамилия"] = "Иванов"

print(my_dict)
