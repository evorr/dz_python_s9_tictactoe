# gitigore !!!!!!!!!!
# requirements !!!!!!!

import random
import emoji
from prettytable import PrettyTable


def get_player_name():
    player = input('Введите ваше имя: ')
    bot = 'Computer'
    return player, bot


def first_move():
    player1, player2 = get_player_name()
    if random.randint(0, 1) == 1:
        print(f'Первым делает ход {player1} - X')
        return player1, player2
    else:
        print(f'Первым делает ход {player2} - X')
        return player2, player1


def create_grid():
    weight, height = 3, 3
    grid = [[1 for x in range(weight)] for y in range(height)]
    k = 1
    for j in range(len(grid)):
        for i in range(len(grid)):
            grid[j][i] = i + k
        k += 3
    return grid


def print_grid(grid):
    x = PrettyTable()
    x.border = False
    x.header = False
    for i in range(len(grid)):
        x.add_row(grid[i])
    print(x)


def get_number(player, used_numders):
    if player == 'Computer':
        number_comp = random.randint(1, 9)
        if number_comp not in used_numders:
            print('Ходит Computer:')
            return number_comp
        else:
            return get_number(player, used_numders)
    else:
        number_user = int(input('Введите номер клетки: '))
        return number_user


def replace(number, matrix, value):
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            if matrix[j][i] == number:
                matrix[j][i] = value


def check_trio(matrix, used_numb):
    for j in range(len(matrix)):
            if matrix[j][0] == matrix[j][1] == matrix[j][2]:
                return matrix[j][0]
    for i in range(len(matrix)):
            if matrix[0][i] == matrix[1][i] == matrix[2][i]:
                return matrix[0][i]
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        return matrix[0][0]
    elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return matrix[0][2]
    elif len(used_numb) == 9:
        return 'Draw'
    else:
        return 'con'


def end_game(dict_marks, stop):
    for k, v in dict_marks.items():
        if v == stop:
            return f'{k} - выиграл'
        else:
            return 'ничья'


def start_game():
    fir_player, sec_player = first_move()
    dict_marks = {fir_player: emoji.emojize(":cross_mark:"),
                  sec_player: emoji.emojize(":hollow_red_circle:")
                  }
    grid = create_grid()
    print_grid(grid)
    used_numbers = []
    stop = 'con'
    while stop not in [emoji.emojize(":cross_mark:"), emoji.emojize(":hollow_red_circle:"), 'Draw']:
        number = get_number(fir_player, used_numbers)
        replace(number, grid, dict_marks[fir_player])
        print_grid(grid)
        print()
        used_numbers.append(number)
        stop = check_trio(grid, used_numbers)
        if stop not in [emoji.emojize(":cross_mark:"), emoji.emojize(":hollow_red_circle:"), 'Draw']:
            number = get_number(sec_player, used_numbers)
            replace(number, grid, dict_marks[sec_player])
            print_grid(grid)
            print()
            used_numbers.append(number)
            stop = check_trio(grid, used_numbers)
    result = end_game(dict_marks, stop)
    print(result)