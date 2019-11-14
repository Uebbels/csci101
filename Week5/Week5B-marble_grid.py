#Brendan Uebelhoer
#CSCI 102 Section C
#week 5 Part B

import random
random.seed()
cords = []
hieght = int(input('HIEGHT>'))
width = int(input('WIDTH>'))

print('In the following grid')

for h in range(hieght):
    #print(h)
    for w in range(width):
        #print(w)
        random_num = random.randint(1,2)
        if random_num == 2:
            print('O', end = ' ')
            t = (h,w)
            cords.append(t)
        else:
            print('X', end = ' ')
    print()

print('The marbles are at')
print('OUTPUT',cords)            