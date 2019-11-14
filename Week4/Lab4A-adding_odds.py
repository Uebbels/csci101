#Brendan Uebelhoer
#CSCI 102- Section C
#Week- part A

a = 0
b = 0
sum = 0
num = 0

print('please input two numbers:')
a = int(input('FIRST>'))
b = int(input('SECOND>'))

if a % 2 == 1:
    num = a
else:
    num = a + 1

while num <= b:
    sum += num
    num += 2

print('the sum of your numbers is %d' % sum)
print('OUTPUT %d' % sum)
