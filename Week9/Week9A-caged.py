#Brendan Uebelhoer
#CSCI 102 Section C
#week 9 Part A

with open('caged.txt','r') as file:
    caged = file.read()

caged_converted = []
for i in caged:
    if i == '&':
        caged_converted.append('%')
    elif i == '%':
        caged_converted.append('&')
    elif i == '/':
        caged_converted.append('~')
    else:
        caged_converted.append(i)
caged_converted = ''.join(caged_converted)


with open('caged_converted.txt','x') as file:
    file.write(caged_converted)
