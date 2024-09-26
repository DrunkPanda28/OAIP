number = int(input("Введите номер буквы (от 1 до 26): ")) - 1

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Находим нужную букву и следующие три
result = []
for i in range(4):
    # Используем модуль для циклического перехода
    result.append(alphabet[(number + i) % 26])

print("".join(result))
