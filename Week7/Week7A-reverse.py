#Brendan Uebelhoer
#CSCI 102 Section C
#Week 7-Part A

N = 0

print('Please input the size of your array')
N = int(input('SIZE>'))
counter = 1

output = [0] * N
reversed_output = output

for i in range(N):
    list = [0] * N
    for j in range(N):
        list[j] = counter
        counter += 1
    output[i] = list

print('\nThe original list is:')
for i in range(N):
    print(output[i])
    
for i in range(N):
    output[i].reverse()
output.reverse()
    
print('\nThe reversed list is:')
for i in range(N):
    print(output[i])


counter = 1

output = [0] * N

for i in range(N):
    list = [0] * N
    for j in range(N):
        list[j] = counter
        counter += 1
    output[i] = list

print('\nThe original list is:')
for i in range(N):
    print(output[i])    
    
for i in range(N):
    output[i] = reversed_output[-i]

print('\nThe reversed list is:')
for i in range(N):
    print(reversed_output[i])
