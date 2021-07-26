import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='X'
p2s='O'

def place(symbol):
    print(numpy.matrix(board))
    while 1:
        row=int(input("Enter row - 1,2 or 3"))
        col=int(input("Enter column - 1,2 or 3"))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break
    board[row-1][col-1]=symbol

def won(symbol):
    return check_rows(symbol) or check_col(symbol) or check_diag(symbol)

def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,' WON ')
            return True
    return False

def check_col(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,' WON ')
            return True
    return False

def check_diag(symbol):
    if board[0][2]==board[1][1] and board[2][0]==board[1][1] and board[1][1]==symbol:
        print(symbol,' WON ')
        return True
    elif board[0][0]==board[1][1] and board[2][2]==board[1][1] and board[1][1]==symbol:
        print(symbol,' WON ')
        return True
    return False



def play():
    for turn in range(9):
        if turn%2==0:
            print('X Turn')
            place(p1s)
            if won(p1s):
                break
        else:
            print('O Turn')
            place(p2s)
            if won(p2s):
                break

    if not(won(p1s)) and not(won(p2s)):
        print('____________DRAW_____________')

        

play()



