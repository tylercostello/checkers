board=[0]*64
#0 is an empty space
#1 is a black checker
#2 is a red checker
#3 is a black king
#4 is red king

"""
0  1  2  3  4  5  6  7 
8  9  10 11 12 13 14 15 
16 17 18 19 20 21 22 23 
24 25 26 27 28 29 30 31 
32 33 34 35 36 37 38 39 
40 41 42 43 44 45 46 47 
48 49 50 51 52 53 54 55 
56 57 58 59 60 61 62 63 
"""
def moveDown(board, start, end, enemy):
    #black pieces
    if (end-start==9 and start%8 != 7) or (end-start==7 and start%8!=8):
        if board[end]==0:
            #valid move
            board[end]=board[start]
            board[start]=0
            wasTake=False
            return True
    elif (end-start==18 and start%8 < 6):
        if board[start+9]%2==enemy and board[end]==0:
            board[end]=board[start]
            board[start+9]=0
            board[start]=0
            wasTake = True
            return True
    elif (end-start==14 and start%8 > 2):
        if board[start+7]%2==enemy and board[end]==0:
            board[end]=board[start]
            board[start+7]=0
            board[start]=0
            wasTake = True
            return True
        else:
            print(board[start+7]%2)
            print(board[end])
    print("Invalid")
    return False

def moveUp(board, start, end, enemy):
    #red pieces
    if (start-end==9 and end%8 != 7) or (start-end==7 and end%8!=8):
        if board[end]==0:
            #valid move
            board[end]=board[start]
            board[start]=0
            wasTake = False
            return True
    elif (start-end==18 and end%8 < 6):
        if board[start-9]==enemy and board[end]==0:
            board[end]=board[start]
            board[start-9]=0
            board[start]=0
            wasTake = True
            return True
    elif (start-end==14 and end%8 > 2):
        if board[start-7]==enemy and board[end]==0:
            board[end]=board[start]
            board[start-7]=0
            board[start]=0
            wasTake = True
            return True
    print("Invalid")
    return False

def makeMove(board, start, end, player):
    if player==1:
        #black pieces
        if board[start]==1:
            moveDown(board, start, end, 0)
        elif board[start]==3:
            if end-start>0:
                moveDown(board, start, end, 0)
            elif end-start<0:
                moveUp(board, start, end, 0)
            else:
                print("Invalid")
                return False
    elif player==2:
        #red pieces
        if board[start]==2:
            moveUp(board, start, end, 1)
        elif board[start]==4:
            if end-start>0:
                moveDown(board, start, end, 1)
            elif end-start<0:
                moveUp(board, start, end, 1)
            else:
                print("Invalid")
                return False


def printBoard(board):
    for i in range(len(board)):
        print(board[i], end =" ")
        if i%8==7:
            print("")
def isOver(board):
    if 1 not in board and 3 not in board:
        return 2
    elif 2 not in board and 4 not in board:
        return 1
    else:
        return 0




for i in range(1,8,2):
    board[i]=1
for i in range(8,16,2):
    board[i]=1
for i in range(17,24,2):
    board[i]=1

for i in range(40,48,2):
    board[i]=2
for i in range(49,56,2):
    board[i]=2
for i in range(56,64,2):
    board[i]=2

playerTurn=1
wasTake=False
while isOver(board)==0:

    if playerTurn==1:
        printBoard(board)
        print("Player 1")
        start = int(input("Type current piece position or -1 to end turn: "))
        end = int(input("Type final piece position: "))
        if start==-1:
            playerTurn=2
        else:
            makeMove(board, start, end, 1)
        if wasTake==False:
            playerTurn=2

    if playerTurn==2:
        printBoard(board)
        print("Player 2")
        start = int(input("Type current piece position or -1 to end turn: "))
        end = int(input("Type final piece position: "))
        makeMove(board, start, end, 2)
        if wasTake==False:
            playerTurn=1
if isOver(board)==1:
    print("player 1 wins")
elif isOver(board)==2:
    print("player 2 wins")


"""
while gameNotOver:
    player1Turn()
    if take
        Player1
    else
        player2
        if take
            player2
    updateisover
"""