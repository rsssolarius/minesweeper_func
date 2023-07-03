# Реализуем игру Сапёр функциональным программированием

import random
N, M = 5, 5

def show(field):
    """Отображает игровое поле (список) графически"""
    for i in range(N):
        for j in range(N):
            print(str(field[i * N + j]).rjust(3), end='')
        print()

def count_mines(field_m, i, j):
    """Функция обсчитывает число мин вокруг клетки и возвращает целое число (1, 2, 3 и т.д.)"""
    n = 0   # Количество мин вокруг клетки (изначально 0)
    for x in range(-1, 2):
        for y in range(-1, 2):
            k = i + x
            l = j + y
            if k < 0 or k >= N or l < 0 or l >= N:
                continue
            if field_m[k * N + l] == 'x':
                n += 1
    return n


def create_field(field_m):
    """Создает игровое поле (список field_p) и поле с минами(список field_m). N - размерность квадратного поля, M - число мин в игре"""

    rng = random.Random()
    n = M
    while n > 0:
        i = rng.randrange(N)    # Случайное целое число в диапазоне [0, N - 1]
        j = rng.randrange(N)
        if field_m[i * N + j] == 'o':
            field_m[i * N + j] = 'x'
            n -= 1

    # Необходимо вычислить число мин вокруг клетки
    for i in range(N):
        for j in range(M):
            if field_m[i * N + j] == 'o':
                field_m[i * N + j] = count_mines(field_m, i, j)



def player_move():
    """Ход игрок: введение им координат клетки ("x y"), проверка на корректность"""
    flag_loop = True
    while flag_loop:
        x, y = input('Введите координаты клетки через пробел: ').split()

        if not x.isdigit() or not y.isdigit():
            print('Координаты введены неверно')
            continue

        x = int(x) - 1
        y = int(y) - 1
        if x < 0 or x >= N or y < 0 or y >= N:
            print(f'Координаты выходят за пределы поля {N}x{N}')
            continue

        flag_loop = False
    return x, y


def game_over(field_m, field_p, x, y):
    """Проверка состояния игры: игра завершена (игрок попал на мину или все клетки без мин открыты) или игра продолжается"""   
    if field_m[x * N + y] == 'x':
        print('Вы взорвались! Игра окончена.')
        return False
    
    else:
        field_p[x * N + y] = field_m[x * N + y]

    count = 0   # Подсчитываем неоткрытые '?'
    for i in range(N):
        for j in range(N):
            if field_p[i * N + j] == '?':
                count += 1
    if count == M:
        print('Поздравляем! Вы обезвредили все мины!')
        return False    # Игра завершилась, т.к. остались неоткрытыми только клетки с минами (в количестве M)
    return True    # Игра продолжается

    


def start_game():
    """Данная функция является самой верхнеуровневой: запуск игры.
    Отображается игровое поле, игрок вводит закрытую клетку, происходит проверка на наличие мины, игра продолжается или завершается"""

    field_p = ['?'] * N * N     # ? - закрытая клетка, начальное игровое поле
    field_m = ['o'] * N * N     # o - клетка без мины, начальное поле "админа"
    create_field(field_m)
    show(field_p)
    #print()
    #show(field_m)
    x, y = player_move()
    while game_over(field_m, field_p, x, y):
        field_p[x * N + y] = field_m[x * N + y]
        show(field_p)
        #print()
        #show(field_m)
        x, y = player_move()

start_game()
print('игра завершена///')