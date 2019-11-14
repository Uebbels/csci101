#Brendan Uebelhoer
#CSCSI 102 Section C
#Week 5 Part C

A = 0
C = 0
G= 0
T = 0
error = False

print('Please input a DNA string of length less than 100')
DNA = input('STRING>')
RNA = ''

for i in DNA:
    if i == 'A':
        A += 1
        RNA += i
    elif i == 'C':
        C += 1
        RNA += i
    elif i == 'G':
        G += 1
        RNA += i
    elif i == 'T':
        T +=  1
        RNA += 'U'
    else:
        error = True
        break



if error == False:
    print('OUTPUT %d %d %d %d' % (A,C,G,T))
    print('OUTPUT', RNA)
if error == True:
    print('OUTPUT DNA string not valid')
     