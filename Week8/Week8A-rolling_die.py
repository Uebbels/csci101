
#Brendan Uebelhoer
#CSCI 102 - Section C
#Week 8 Part A

import random

num = 0
rolls = 0
count = [0,0,0,0,0,0]

rolls = int(input('Please input the number of rolls you would like to make:\nROLLS>'))

for i in range(rolls):
    num = random.randint(1,6)
    #print(num)
    count[num-1] += 1
    #print(count)
