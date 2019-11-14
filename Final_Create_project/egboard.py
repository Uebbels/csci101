import csv
import datetime
import os

def printboard(printedboard):	  #prints out the parameterized board board
    r=0
    print(' ', end = ' ')
    for i in range(len(printedboard[0])):
        print(i, end = ' ')
    print()
    for i in printedboard:
        print(r, end = ' ')
        r += 1
        for j in i:
            if j == -1:
                print(' ', end=' ')
            if j == 0:
                print('o', end=' ')
            if j == 1:
                print('i', end=' ')
            if j == 2:
                print('I', end=' ')
        print()

def getboard(file):	    #imports a board to a nested list from a .csv file
    with open(file,'r') as csvfile:
        board = []
        i=0
        boardreader = csv.reader(csvfile)
        for row in boardreader:
            board.append([])
            board[i] = row
            j = 0
            for spot in board[i]:
                board[i][j] = int(spot)
                j += 1
            i += 1
    return board

def removepeg(x,y):     #removes a peg at the given location if one exists and replaces it with an open spot
    if currentboard[y][x] == 1:
        currentboard[y][x] = 0
    else:
        print('error, could not replace peg: location not peg: location (%d,%d) is %s' % (x,y,currentboard[y][x]))

def addpeg(x,y):
    if currentboard[y][x] == 0:
        currentboard[y][x] = 1
    else:
        print('error, could not add peg: location not hole: location (%d,%d) is %s' % (x,y,currentboard[y][x]))

def checkmove(move):
    x1 = move[0]
    y1 = move[1]
    x2 = move[4]
    y2 = move[5]
    if (0 <= x1 < len(currentboard[0])) and (0 <= x2 < len(currentboard[0])) and (0 <= y1 < len(currentboard)) and (0 <= y2 < len(currentboard)):
        if currentboard[y1][x1] == 1 and currentboard[y2][x2] == 0:
        
            if ((x1-x2) == 2 and y2==y1):
                if currentboard[y1][x1-1] == 1:
                    return True
            elif ((x1-x2) == -2 and y2==y1):
                if currentboard[y1][x1+1] == 1:
                    return True
            elif ((y1-y2) == 2 and x1==x2):
                if currentboard[y1-1][x1] == 1:
                    return True
            elif ((y1-y2) == -2 and x1==x2):
                if currentboard[y1+1][x1] == 1:
                    return True
            else:
                return False
        else:
            return False

def getmove(x,y,direction):
    move=[0,0,0,0,0,0]
    move[0] = x
    move[1] = y
    if direction == 'up':
        move[2] = move[0]
        move[3] = move[1] -1        
        move[4] = move[0]
        move[5] = move[1] - 2
    if direction == 'down':
        move[2] = move[0]
        move[3] = move[1] + 1
        move[4] = move[0]
        move[5] = move[1] + 2
    if direction == 'right':
        move[2] = move[0] + 1
        move[3] = move[1]
        move[4] = move[0] + 2
        move[5] = move[1] 
    if direction == 'left':
        move[2] = move[0] - 1
        move[3] = move[1]
        move[4] = move[0] - 2
        move[5] = move[1]
    return move

def getallmoves():
    allmoves = []
    for i in range(len(currentboard)):
        for j in range(len(currentboard[i])):
            for d in ['up','down','right','left']: 
                testmove = getmove(j, i, d)
                if checkmove(testmove):
                    allmoves.append(testmove)
    return allmoves

def executemove():
    printboard(currentboard)
    print('You have %d pegs remaining!' % countpegs(currentboard))
    print('Your Next move')
    x = int(input('X:'))
    y = int(input('Y:'))
    direction = input('Would you like to jump up, down, left, or right\n')
    move = getmove(x,y,direction)
    if checkmove(move):
        removepeg(move[0], move[1])
        removepeg(move[2], move[3])
        addpeg(move[4], move[5])
    else:
        print('move failed, invalid move')

def countpegs(countedboard):
    pegcount = 0
    for i in countedboard:
        for j in i:
            if j == (1 or 2):
                pegcount += 1
    return pegcount


print('Welcome to Egboard! to start please select your difficulty!')
#difficulty = input('FIXME!')
print('What board would you like to play with?\n'
      '1-cross\n'
      '2-asymmetric cross\n'
      '3-small cross\n'
      '4-round\n'
      '5-diamond\n'
      '6-triangle\n'
      '7-custom')
boardoption = int(input('board:'))        
if boardoption == 1:
    boardfile = 'cross.csv'
elif boardoption == 2:
    boardfile = 'asymmetric_cross.csv'
elif boardoption == 3:
    boardfile = 'small_cross.csv'
elif boardoption == 4:
    boardfile = 'round.csv'
elif boardoption == 5:
    boardfile = 'diamond.csv'
elif boardoption == 6:
    boardfile = 'triangle.csv'
elif boardoption == 7:
    boardfile =input ('please input the filename of the custom board file:\n')

boardfile = os.path.join('boards',boardfile)


currentboard = getboard(boardfile)

while len(getallmoves()) > 0:
    executemove()