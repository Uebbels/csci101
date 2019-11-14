#Brendan Uebelhoer
#CSCI 102 Section C
#Week 6 Part A
'''
Python uses white space to reduce the redundancy in syntax. Standard formatting in every
other language requires that the code be formatted identically to python's requirements.
By simply making that formatting a part of the language, it removes the redundancy of
needing to also put in other syntax indications, such as { and }.
'''
print("enter a number to generate it's Corllatz Conjecture")
num = int(input('NUMBER>'))
con = [num]

while num > 1:
    if num % 2 == 1:
        num = (3 * num) + 1
    else:
        num /= 2
    num = int(num)
    con.append(num)

print('OUTPUT',*con)