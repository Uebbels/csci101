import csv
import time
import os
import sys

def printboard(printedboard):	  #prints out the parameterized board
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
    if currentboard[y][x] == (1 or 2):
        currentboard[y][x] = 0
    else:
        print('error, could not replace peg: location not peg: location (%d,%d) is %s' % (x,y,currentboard[y][x]))

def addpeg(x,y):        #adds a peg at the given location if it is a valid location
    if currentboard[y][x] == 0:
        currentboard[y][x] = 1
    else:
        print('error, could not add peg: location not hole: location (%d,%d) is %s' % (x,y,currentboard[y][x]))

def checkmove(move):    #checks if a given move is a valid move to make on the current board
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

def getmove(x,y,direction): #inputs a move from the user
    move=[0,0,0,0,0,0]
    move[0] = x
    move[1] = y
    if direction == 'u':
        move[2] = move[0]
        move[3] = move[1] -1        
        move[4] = move[0]
        move[5] = move[1] - 2
    if direction == 'd':
        move[2] = move[0]
        move[3] = move[1] + 1
        move[4] = move[0]
        move[5] = move[1] + 2
    if direction == 'r':
        move[2] = move[0] + 1
        move[3] = move[1]
        move[4] = move[0] + 2
        move[5] = move[1] 
    if direction == 'l':
        move[2] = move[0] - 1
        move[3] = move[1]
        move[4] = move[0] - 2
        move[5] = move[1]
    return move

def getallmoves():      #returns a list of all valid moves a user can make
    allmoves = []
    for i in range(len(currentboard)):
        for j in range(len(currentboard[i])):
            for d in ['u','d','r','l']: 
                testmove = getmove(j, i, d)
                if checkmove(testmove):
                    allmoves.append(testmove)
    return allmoves

def executemove():      #main logic of the game, inputs move, checks validity, and if valid executes the move
    printboard(currentboard)
    if move_counter != 1:
        print('You have made %d moves!' %move_counter)
    else:
        print('You have made %d move!' %move_counter)
    print('You have %d pegs remaining!' % countpegs(currentboard))
    print('Your next move')
    x = int(input('X:'))
    y = int(input('Y:'))
    direction = input('Would you like to jump up, down, left, or right\n')
    move = getmove(x,y,direction)
    move_list.append(move)
    if checkmove(move):
        removepeg(move[0], move[1])
        removepeg(move[2], move[3])
        addpeg(move[4], move[5])
    else:
        print('move failed, invalid move')

def countpegs(countedboard): #counts the numbner of pegs currently on the board
    pegcount = 0
    for i in countedboard:
        for j in i:
            if j == (1 or 2):
                pegcount += 1
    return pegcount

move_counter = 0
move_list = []
print('Welcome to Egboard!')
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
    boardfile =input ('please input the filename of the custom board file:\n') + '.csv'

boardfile = os.path.join(sys.path[0],'boards',boardfile)

currentboard = getboard(boardfile)

start = time.time()

while len(getallmoves()) > 0:
    executemove()
    move_counter += 1

printboard(currentboard)

print('No moves remaining!')
end = time.time()
if countpegs(currentboard) == 1:
    print('One peg left! You have beaten this board using %d moves in %.2f seconds!' %(move_counter, (end-start)))
else:
    print('%d pegs remaining using %d moves in %.2f seconds! good job!' % (countpegs(currentboard), move_counter, (end-start)))

print('Thanks for playing!')
