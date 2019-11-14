#Brendan Uebelhoer
#CSCI 102 Section C
#week 5 Part A

print('please input a random string of Xs and Os')
string = input('STRING>')
locations = []
cords = 0

for i in string:
    if i == 'O':
        locations.append(cords)
    cords += 1
print('I have found your marbles! They are at')
print('OUTPUT',locations)