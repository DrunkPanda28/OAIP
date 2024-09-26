word = input("Введите слово: ")

# Определяем длину слова
length = len(word)

# Проверяем, четная или нечетная длина

if length % 2 == 1:  # Если длина нечетная
    middle_index = length // 2
    result = word[middle_index]
else:  # Если длина четная
    result = word[length // 2 - 1]


print("Результат:", result)
