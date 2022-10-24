def greed():
    print("-" * 20)
    print("  Добро пожаловать  ")
    print("       в игру       ")
    print("  Крестики-нолики   ")
    print("-" * 20)
    print(" формат ввода: х, у ")
    print("х - это номер строки")
    print("у - номер столбца   ")

def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  ________________")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  ________________")
    print()

def ask():
    while True:
        cords = input("      Ваш ход: ").split()
        if len(cords) != 2:
            print("Введите 2 коордираты! ")
            continue
        x, y = cords
        if not(x.isdigit()) or not (y.isdigit()):
            print("Введите числа! ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона, введите другие! ")
            continue
        elif field[x][y] != "-":
            print("Клетка занята! ")
            continue
        return x, y

def chek_win():
    wins = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
            ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
            ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)))
    for cord in wins:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Х!!")
            return True
        if symbols == ["O", "O", "O"]:
            print("Выиграл O!!")
            return True
    return False
def start():
    num = 0
    while True:
        num +=1
        show()
        if num % 2 == 1:
            print("Ходит крестик ")
        else:
            print("Ходит нолик ")
        x, y = ask()
        if num % 2 == 1:
            field[x][y] = "X"
        else:
            field[x][y] = "O"
        if chek_win():
            break
        if num == 9:
            print("Ничья!")
            break

field = [["-"] * 3 for i in range(3)]
greed()
start()