import random

# Варианты хода
variants = ["камень", "ножницы", "бумага"]

# Выйгрышные комбинации
rules = {
    "камень":"ножницы",
    "ножницы":"бумага",
    "бумага":"камень"
    }

# Счётчик игры
wins = 0
losses = 0
draws = 0

print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
print("Доступные ходы: камень, ножницы, бумага.")
print("Для выхода введите 'выход' или 'exit'.\n")

while True:
    # Ввод игрока
    player = input("Ваш ход: ").strip().lower()

    # Проверка на выход из игры
    if player in ("выход", "exit"):
        print("\nИгра завершена.")
        print(f"Итоговый счёт: Побед: {wins}, Поражений: {losses}, Ничьих: {draws}")
        print("Спасибо за игру!")
        break

    # Проверка корректности ввода
    if player not in variants:
        print("Некорректный ввод. Попробуйте ещё раз.\n")
        continue

    # Ход компьютера
    computer_choice = random.choice(variants)
    print(f"Компьютер выбрал: {computer_choice}")

    # Определение результата
    if player == computer_choice:
        result = "Ничья!"
        draws += 1
    elif rules[player] == computer_choice:
        result = "Вы победили!"
        wins += 1
    else:
        result = "Компьютер победил!"
        losses += 1

    # Вывод результата и текущего счёта
    print(result)
    print(f"Счёт: Побед {wins} - {losses} Поражений, Ничьих: {draws}\n")
