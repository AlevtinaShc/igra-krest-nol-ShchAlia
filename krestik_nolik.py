def igra():
    print(" ")
    print("     Здравствуйте!!!   ")
    print("    Давайте поиграем   ")
    print("   в крестики - нолики ")
    print("  * * * * * * * * * * *")
    print("    формат ввода: x, y ")
    print("  x - это номер строки ")
    print("  y - это номер столбца")

# вывод игрового поля на экран
field = [[" "] * 3 for i in range(3)]
def table():
    print()
    print("     | 0 | 1 | 2 | ")
    print("   ----------------")
    for i, row in enumerate(field):
        row_str = f"  {i}  | {' | '.join(row)} |"
        print(row_str)
        print("   ----------------")

# запрашиваем координаты у игрока
# X - это большая латинская буква X
# 0 - это цифра 0
def guestion():
    while True:
        komment = input("     Ваш ход! ").split()
        if len(komment) != 2:
            print("  Введите две координаты! ")
            continue

        x, y = komment
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Коордтнаты вне игрового поля! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue
        return x, y

# проверка выигрышных комбинаций
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for komment in win_cord:
        symbols = []
        for c in komment:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print(" Выиграл крестик! ")
            return True
        if symbols == ["0", "0", "0"]:
            print(" Выиграл нолик! ")
            return  True
    return False

igra()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    table()
    if count % 2 == 1:
        print(" Ходит крестик! ")
    else:
        print(" Ходит нолик! ")

    x, y = guestion()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" НИЧЬЯ!! ")
        break