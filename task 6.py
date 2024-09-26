review = input("Введите отзыв: ")

# Разделяем отзыв на слова
words = review.split()

# Список для хранения имен сотрудников
names = []

# Ищем слова, которые начинаются с заглавной буквы
for word in words:
    if word.istitle():
        names.append(word)

# Объединяем имена в одну строку, разделяя запятыми
result = '/'.join(names)

# Выводим результат
print("Назначить премию:", result)
