# Создаем пустое множество
empty_set = set()

print(empty_set)

# Создаем множество с элементами
elements_set = {1, 6, 2, 3, 4, 8, 5}

print(elements_set)


# Создаем пустое множество
my_set = set()

# Добавляем элементы
my_set.add(1)
my_set.add(5)
my_set.add(8)

print(my_set)


#Разность множеств
set_g = elements_set - my_set

print(set_g)

#Очищение множества
set_g.clear()
print(set_g)

# Создание копии
set_k = my_set.copy()
print(set_k) 
