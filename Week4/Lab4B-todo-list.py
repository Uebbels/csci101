#Brendan Uebelhoer
#CSCI 102 Section C
#Week 4- Part B

counter = 0
task = ' '
lots_to_do = 7
not_much_to_do = 4

print('enter tasks to do, type "DONE" when you are finished')
task = input('TASK>')

while task != 'DONE':
    counter += 1
    task = input('TASK>')

print('OUTOUT',counter)

if counter < not_much_to_do:
    print('OUTPUT FREE')
elif counter > lots_to_do:
    print('OUTPUT BUSY')
else:
    print('OUTPUT MODERATELY')
    
