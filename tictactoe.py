theBoard = {'tl': ' ', 'tm': ' ', 'tr': ' ',
'ml': ' ', 'mm': ' ', 'mr': ' ',
'll': ' ', 'lm': ' ', 'lr': ' '}

def printBoard(board):
    print(board['tl'] + '|' + board['tm'] + '|' + board['tr'])
    print('-+-+-')
    print(board['ml'] + '|' + board['mm'] + '|' + board['mr'])
    print('-+-+-')
    print(board['ll'] + '|' + board['lm'] + '|' + board['lr'])
    
printBoard(theBoard)

turn = "X"

for i in range(9):
    print("Enter you choice")
    move = input()
    theBoard[move] = turn
    printBoard(theBoard)
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
