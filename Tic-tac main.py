from random import randint

#константа для обработки в "цифру"
vertical_coordinats = ('a''b''c')

def get_user_symb():
    user_symb = input('Выберете символ (x, 0 ):').strip('').lower()
    while user_symb not in ('x','0'):
        print ('Неверный символ.')
        user_symb = input('Выберете символ (x, 0 ):').strip('').lower()
    return user_symb

#Игровое поле:
def show_board(board):
    print(' ','1','2','3')
    for y, v in enumerate(vertical_coordinats):
        print(v,''.join(board [y]))


#Ход компьютера
def get_computer_position(board):
    x, y = randint(0, 2), randint(0, 2)
    while board[y][x] != '_':
        x, y = randint(0, 2), randint(0, 2)
    return x, y

#Ход игрока
def get_user_position(board):
    real_x, real_y = 0, 0
    while True:
        coordinats = input('Введите координаты').lower().strip(' ')
        y, x = tuple(coordinats)

        if int(x)not in (1,2,3) or y not in vertical_coordinats:
            print('Неправильные координаты.')
            continue

        real_x, real_y = int(x) - 1, vertical_coordinats.index(y)
        if board[real_y][real_x] == '_':
            break
        else:
            print('Эта позиция уже занята')
    return real_x, real_y

def get_opponent_symb(symb):
    return '0' if symb == 'x' else 'x'

#Победа или поражение
def is_win(symb, board):
    opponent_symb = get_opponent_symb(symb)
    #Проверка строки
    for y in range(3):
        if opponent_symb not in board[y] and '_' not in board[y]:
            return True
    #Проверка колонки
    for x in range(3):
        col = [board[0][x], board[1][x], board[2][x]]
        if opponent_symb not in col and '_' not in col:
            return True
    #Проверка диагонали
    diagonal = [board[0][0], board[1][1], board[2][2]]
    if opponent_symb not in diagonal and '_' not in diagonal:
        return True
    diagonal = [board[0][2], board[1][1], board[2][0]]
    if opponent_symb not in diagonal and '_' not in diagonal:
        return True

    return False

#Ничья
def is_draw(board):
    count = 0
    for y in range(3):
       count += 1 if '_' in board[y] else 0
    return count == 0

#Поле
board = [
    ['_ '  for x in range(3)] for y in range(3)
]

user_symb = get_user_symb()
computer_symb = get_opponent_symb(user_symb)

#Игровой цикл
while True:
    show_board(board)
    if is_draw(board):
        print('ничья')
        break



    x, y = get_user_position(board)
    board[y][x] = user_symb
    if is_win(user_symb, board):
        print('Вы победили!')
        break

    x, y = get_computer_position(board)
    board[y][x] = computer_symb
    if is_win(computer_symb, board):
        print('Вы проиграли!')
        break

