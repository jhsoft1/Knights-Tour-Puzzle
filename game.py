import copy
import math

MOVES = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
targets = [str(k) for k in range(8)] + ['_']
no_more = False
squares_visited = 0


def next_move(message, i_board):
    global no_more
    if squares_visited == X * Y:
        print('What a great tour! Congratulations!')
        exit()
    if no_more:
        print('No more possible moves!')
        print('Your knight visited', squares_visited, 'squares!')
        exit()
    while True:
        try:
            a, b = (int(z) - 1 for z in input(message).split())
            assert i_board[b][a][-1] in targets
        except (ValueError, AssertionError, IndexError):
            print('Invalid move!', end=' ')
        else:
            if i_board[b][a][-1] == '0':
                no_more = True
            return a, b


def show_possibilities(i_board):
    min_distinct_moves, min_y0, min_x0 = 8, -100, -100
    for move in MOVES:
        y0, x0 = y + move[0], x + move[1]
        if 0 <= y0 < Y and 0 <= x0 < X:
            distinct_moves = 0
            for move1 in MOVES:
                y1, x1 = y0 + move1[0], x0 + move1[1]
                if 0 <= y1 < Y and 0 <= x1 < X and i_board[y1][x1][-1] != '*': distinct_moves += 1
            if i_board[y0][x0][-1] != '*':
                i_board[y0][x0] = ' ' * (len_placeholder - 1) + str(distinct_moves - 1)
                if distinct_moves < min_distinct_moves:
                    min_distinct_moves = distinct_moves
                    min_x0, min_y0 = x0, y0
    print(' ---' + '-' * (len_placeholder + 1) * X)
    for i in range(Y - 1, -1, -1):
        print(i + 1, '| ', *(i_board[i][j] + ' ' for j in range(X)), '|', sep='')
    print(' ---' + '-' * (len_placeholder + 1) * X)
    print('  ', *(j for j in range(1, X + 1)), '\n', sep=' ' * len_placeholder)
    return min_x0, min_y0, i_board


while True:
    try:
        X, Y = (int(x) for x in input("Enter your board dimensions:").split())
        assert X > 0 and Y > 0
    except (ValueError, AssertionError):
        print('Invalid dimensions!')
    else:
        break
len_placeholder = int(math.log(X * Y, 10)) + 1
board = [['_' * len_placeholder] * X for _ in range(Y)]
x, y = next_move("Enter the knight's starting position:", board)
board[y][x] = ' ' * (len_placeholder - 1) + 'X'
targets.pop()
while True:
    min_x, min_y, show_board = show_possibilities(copy.deepcopy(board))
    board[y][x] = ' ' * (len_placeholder - 1) + '*'
    squares_visited += 1
    x, y = min_x, min_y  # next_move("Enter your next move:", show_board)
    board[y][x] = ' ' * (len_placeholder - 1) + 'X'
