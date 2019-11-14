#Brendan Ueblehoer
#CSCI 102 Section C
#Week 10 Part A
import random

def printlist(list):
    for i in range(len(list)):
        print('OUTPUT %d occured %d times' %(i+1, list[i]))

def rolldice(rolls):
    num = 0
    count = [0,0,0,0,0,0]
    for i in range(rolls):
        num = random.randint(1,6)
        count[num-1] += 1
    return count

rolls = int(input('Please input the number of rolls you would like to make:\nROLLS>'))
printlist(rolldice(rolls))