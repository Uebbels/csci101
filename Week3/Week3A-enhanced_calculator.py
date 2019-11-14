#Brendan Uebelhoer
#CSCI 102 - Section C
#Week 3 part B

operand_1 = 0.0
operand_2 = 0.0
sum = 0.0
difference = 0.0
product = 0.0
quocient = 0.0
remainder = 0.0

print('First number please')
operand_1 = float(input('FIRST>'))
print('Second number please')
operand_2 = float(input('SECOND>'))
print('Choose one of the folowing operations:\n1 - addition\n2 - subtraction\n3 - multiplication\n4 - division')
operation = int(input('OPERATION>'))

if operation == 1:
    sum = operand_1 + operand_2
    print('The sum of your numbers is',sum)
    print('OUTPUT', sum)

elif operation == 2:
    difference = operand_1 - operand_2
    print('The difference of your number is', differnce)
    print('OUTPUT', difference)

elif operation == 3:
    product = operand_1 * operand_2
    print('The product of your numbers is', product)
    print('OUTPUT', product)

elif operation == 4:
    quotient = operand_1 // operand_2
    remainder = operand_1 % operand_2
    print('The quotient of the numbers is', quotient, 'and the remainder is', remainder)
    print('OUTPUT', quotient)
    print('OUTPUT', remainder)

else:
    print('you made a mistake, please selection a interager between 1 and 4')
