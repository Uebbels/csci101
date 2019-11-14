#Brendan Uebelhoer
#CSCI 102 Sectioc C
#Week 7 Part B

str = input('STRING>')

initial = True
output = ''

for i in str:
    if initial == True:
        output +=i
        initial = False
    if i == "-":
        initial = True

print('OUTPUT',output)