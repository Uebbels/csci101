#Brendan Uebelhoer
#CSCI 102 Section C
#Week 8-Part C

import random
import string

#Initialize Variables: I accidentally flipped the player but i dont wanna go through and fix it, and it work as is

str = ''
stacy_str = ''
kevin_str = ''
winner = 'NULL'
stacy_score = 0
kevin_score = 0
Gamemode = 0
stacy_strings = []
kevin_strings = []
vowels = ['A','E','I','O','U']

#select gamemode, generate string
gamemode = int(input('Would you like to provide your own string or generate a random one? (1 or 2)\nCHOICE>'))

if gamemode == 1:
    str = input('STRING>')
elif gamemode == 2:
    str_list = ['a','b','c','d','e','f]']
    for i in range(6):
        str_list[i] = string.ascii_uppercase[random.randint(0,25)]
    str = ''.join(str_list)
    print('Your random string is %s' % str)
    
#generate all strings and assign them
all_str = [str[i: j] for i in range(len(str)) 
          for j in range(i + 1, len(str) + 1)] 
for i in all_str:
    if i[0] in vowels:
        stacy_strings.append(i)
    else:
        kevin_strings.append(i)

#score them
stacy_score = len(stacy_strings)
kevin_score = len(kevin_strings)
print('OUTPUT %d\nOUTPUT %d' %(stacy_score,kevin_score))
print("Stacey's score is %d and kevin's score is %d" %(kevin_score,stacy_score))

#determine winner
if stacy_score > kevin_score:
    winner = 'KEVIN'
elif kevin_score > stacy_score:
    winner = 'STACEY'
elif kevin_score == stacy_score:
    winner = 'DRAW'
print('OUTPUT',winner)