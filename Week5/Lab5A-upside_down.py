#Brendan Uebelhoer
#CSCI 101 Section B
#Python Lab 5

num = 0
num = int(input('NUMBER>'))

grades = [0] * num
num -=1

for G in grades:
    grades[num] = int(input('GRADES>'))
    num -= 1

print('OUTPUT', grades)
