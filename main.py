from copy import deepcopy

from change import show
kx=3
ky=7
board = [
    ['br', 'bn', 'bb', 'bk', 'bq', 'bb', 'bn', 'br'],
    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
    ['wr', 'wn', 'wb', 'wk', 'wq', 'wb', 'wn', 'wr'],
]
boardcopy=deepcopy(board)
Turn = True

def cord(y1, y2):
    return (6 - y1, 6 - y2)


def output():
    a = 7
    for i in board:
        print(a, *i)
        a -= 1
    print('  1  2  3  4  5  6  7  8')


def change(x2, y2, figure):
    board[y2][x2] = figure
    return figure


def pawngo(x1, y1, x2, y2):
    if 'w' in board[y2][x2]:
        return False

    if y2 == 0:
        figure = show()
        return figure, True
    elif y2 == 4 and y1 == 6 and x1 == x2 and board[y2][x1] == '__' and not ischeck(kx,ky):
        board[6][x1] = '__'
        board[4][x1] = 'wp'
        if ischeck(kx,ky):
            board[6][x1] = 'wp'
            board[4][x1] = '__'
            return False
        return True
        # 2 moves
    elif y1 - y2 == 1 and x2 == x1 and board[y2][x1] == '__' and not ischeck(kx,ky):
        board[y1][x1] = '__'
        board[y2][x2] = 'wp'
        if ischeck(kx,ky):
            board[y1][x1] = 'wp'
            board[y2][x2] = '__'
            return False
        return True
        # 1 move
    elif y1 - y2 == 1 and abs(x2 - x1) == 1 and board[y2][x2] != '__' and not ischeck(kx,ky):
        board[y1][x1] = '__'
        board[y2][x2] = 'wp'
        if ischeck(kx,ky):
            board[y1][x1] = 'wp'
            board[y2][x2] = '__'
            return False
        return True
        # eat move
    else:
        return False


def rook(x1, y1, x2, y2):
    if 'w' in board[y2][x2]:
        return False

    if y1 == y2 and x1 != x2:
        move = True
        for i in range(min(x1, x2) + 1, max(x1, x2)):
            if board[y1][i] != '__' and i != x1:
                move = False
                break
        if move:
            board[y1][x1] = '__'
            board[y2][x2] = 'wr'
            if ischeck(kx,ky):
                board[y1][x1] = 'wr'
                board[y2][x2] = '__'
                return False
    elif x1 == x2 and y1 != y2:
        move = True
        for i in range(min(y1, y2) + 1, max(y1, y2)):
            if board[i][x1] != '__' and i != y1:
                move = False
                break

        if move:
            board[y1][x1] = '__'
            board[y2][x2] = 'wr'
            if ischeck(kx,ky):
                board[y1][x1] = 'wr'
                board[y2][x2] = '__'
                return False
    return move


def bishop(x1, y1, x2, y2):
    if 'w' in board[y2][x2]:
        return False
    if abs(x1 - x2) == abs(y1 - y2):
        b = True
        m = [y for y in range(min(y1, y2) + 1, max(y1, y2) - 1)]
        if len(m) == 0:
            m.append(y2)
        c = m[0]
        for i in range(min(x2, x1) + 1, max((x1, x2)) - 1):
            print(board[c][i])
            if board[c][i] != '__':
                b = False
                break
            c += 1
        if b != False:
            board[y2][x2] = 'wb'
            board[y1][x1] = "__"
            if ischeck(kx,ky):
                board[y2][x2] = '__'
                board[y1][x1] = "wb"
                return False
    return b


def knight(x1, y1, x2, y2):

    if 'w' in board[y2][x2]:
        return False

    if (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1):
        board[y1][x1] = '__'
        board[y2][x2] = 'wn'
        if ischeck(kx,ky):
            board[y1][x1] = 'wn'
            board[y2][x2] = '__'
            return False
        return True
    else:
        return False


def queen(x1, y1, x2, y2):

    if 'w' in board[y2][x2]:
        return False
    move = True

    if y1 == y2 and x1 != x2:

        for i in range(min(x1, x2) + 1, max(x1, x2)):
            if board[y1][i] != '__' and i != x1:
                move = False
                break
        if move:
            board[y1][x1] = '__'
            board[y2][x2] = 'wq'
    elif x1 == x2 and y1 != y2:

        for i in range(min(y1, y2) + 1, max(y1, y2)):
            if board[i][x1] != '__' and i != y1:
                move = False
                break
        if move:
            board[y1][x1] = '__'
            board[y2][x2] = 'wq'
    else:
        if abs(x1 - x2) == abs(y1 - y2):
            b = True
            m = [y for y in range(min(y1, y2) + 1, max(y1, y2) - 1)]
            if len(m) == 0:
                m.append(y2)
            c = m[0]
            print(c)
            for i in range(min(x2, x1) + 1, max((x1, x2)) - 1):
                print(board[c][i])
                if board[c][i] != '__':
                    b = False
                    break
                c += 1
            if b:
                board[y2][x2] = 'wq'
                board[y1][x1] = "__"
            else:
                move = False
        else:
            move = False
    if move:
        if ischeck(kx,ky):
            board[y2][x2] = '__'
            board[y1][x1] = "wq"
            move=False
    return move

def king(x1,y1,x2,y2):
    global kx,ky
    if 'w' not in board[y2][x2]:
        if ((abs(x1-x2)==1 and abs(y1-y2)==1) or (abs(x1-x2)==1 and abs(y1-y2)==0) or (abs(x1-x2)==0 and abs(y1-y2)==1)) and not ischeck(x2,y2):
            board[y1][x1]='__'
            board[y2][x2]='wk'
            kx=x2
            ky=y2
            return True
    return False
def ischeck(x, y):
    # returns True if check exist
    try:
        if board[y-1][x+1]=='bp' or board[y-1][x-1]=='bp':
            return True
    except:
        pass
    try:
        if board[y+1][x+1]=='bk' or board[y-1][x-1]=='bk' or board[y-1][x+1]=='bk' or board[y+1][x-1]=='bk' or board[y][x+1]=='bk' or board[y][x-1]=='bk'or board[y+1][x]=='bk' or board[y-1][x]=='bk':
            return True
    except:
        pass
    x, y = y, x
    try:
        if board[x + 1][y + 2] == 'bn':
            return True
    except:
        pass
    try:
        if board[x + 2][y + 1] == 'bn':
            return True
    except:
        pass
    try:
        if board[x + 2][y - 1] == 'bn':
            return True
    except:
        pass
    try:
        if board[x + 1][y - 2] == 'bn':
            return True
    except:
        pass
    try:
        if board[x - 1][y - 2] == 'bn':
            return True
    except:
        pass
    try:
        if board[x - 2][y - 1] == 'bn':
            return True
    except:
        pass
    try:
        if board[x - 2][y + 1] == 'bn':
            return True
    except:
        pass
    try:
        if board[x - 2][y - 1] == 'bn':
            return True
    except:
        pass
    try:
        if board[x - 2][y - 1] == 'bn':
            return True
    except:
        pass
    try:
        if board[x - 1][y + 2] == 'bn':
            return True
    except:
        pass
    x, y = y, x
    for i in range(x-1, -1, -1):
        if 'w' in board[y][i] or board[y][i] == 'bn' or board[y][i] == 'bp' or board[y][i] == 'bk' or board[y][i] == 'bb':
            break
        if board[y][i] == 'bq' or board[y][i] == 'br':
            return True
    for i in range(x+1, 8):
        if 'w' in board[y][i] or board[y][i] == 'bn' or board[y][i] == 'bp' or board[y][i] == 'bk' or board[y][i] == 'bb':
            break
        if board[y][i] == 'bq' or board[y][i] == 'br':
            return True
    for i in range(y-1, -1, -1):
        if 'w' in board[i][x] or board[i][x] == 'bn' or board[i][x] == 'bp' or board[i][x] == 'bk' or board[i][x] == 'bb':

            break
        if board[i][x] == 'bq' or board[i][x] == 'br':
            return True
    for i in range(y+1, 8):
        if 'w' in board[i][x] or board[i][x] == 'bn' or board[i][x] == 'bp' or board[i][x] == 'bk' or board[i][x] == 'bb':

            break
        if board[i][x] == 'bq' or board[i][x] == 'br':
            return True
    x1, y1 = x, y
    while x1 < 8 and y1 < 8:
        if 'w' in board[y1][x1]:
            break
        if board[y1][x1] == 'wq' or board[y1][x1] == 'wb':
            return True
        x1 += 1
        y1 += 1
    x1, y1 = x, y
    while x1 >= 0 and y1 >= 0:
        if 'w' in board[y1][x1]:
            break
        if board[y1][x1] == 'wq' or board[y1][x1] == 'wb':
            return True
        x1 -= 1
        y1 -= 1
    x1, y1 = x, y
    while x1 < 8 and y1 >= 0:
        if 'w' in board[y1][x1]:
            break
        if board[y1][x1] == 'wq' or board[y1][x1] == 'wb':
            return True
        x1 += 1
        y1 -= 1
    x1, y1 = x, y
    while x1 >= 0 and y1 < 8:
        if 'w' in board[y1][x1]:
            break
        if board[y1][x1] == 'wq' or board[y1][x1] == 'wb':
            return True
        x1 -= 1
        y1 += 1
    return False
