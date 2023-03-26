import random

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print('\n')


def possibleMove(position):
    if board[position] == ' ':
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def checkWin():
    # vertical condition
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True
    # diagonal conditions
    elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] != ' ':
        return True
    # horizontal conditions
    elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True
    else:
        return False


def checkWhichMarkWon(temp):
    # vertical condition
    if board[1] == board[2] and board[1] == board[3] and board[1] == temp:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == temp:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == temp:
        return True
    # diagonal conditions
    elif board[1] == board[5] and board[1] == board[9] and board[1] == temp:
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] == temp:
        return True
    # horizontal conditions
    elif board[1] == board[4] and board[1] == board[7] and board[1] == temp:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == temp:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == temp:
        return True
    else:
        return False


def addLetter(letter, position):
    if possibleMove(position):
        board[position] = letter
        printBoard(board)
        if checkDraw():
            print('Draw')
            exit()
        if checkWin():
            if letter == 'X':
                print('AI Won')
                exit()
            elif letter == 'O':
                print('Humanity Won')
                exit()
        return
    else:
        print("Cannot Enter here")
        position = int(input('Enter new Position : '))
        addLetter(letter, position)
        return


player = 'O'
ai = 'X'


def playerMove():
    position = int(input("Enter Position for O : "))
    addLetter(player, position)
    return


def aiMove():
    bestScore = -1000
    bestMove = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = ai
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key

    addLetter(ai, bestMove)
    return


def minimax(board, depth, isMaximizing):
    if checkWhichMarkWon(ai):
        return 1
    elif checkWhichMarkWon(player):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -1000

        for key in board.keys():
            if board[key] == ' ':
                board[key] = ai
                score = minimax(board, depth+1, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore

    else:
        bestScore = 1000

        for key in board.keys():
            if board[key] == ' ':
                board[key] = ai
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore


print('Computer Plays First')
print('Positions are : ')
print('1 2 3')
print('4 5 6')
print('7 8 9')
print('AI  : X')
print('You : O')
print('\n')

while not checkWin():
    aiMove()
    playerMove()


