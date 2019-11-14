#Brendan Uebelhoer
#CSCI 102 Section C
#Week 7 Part C

print('Enter a DNA string:')
strand = input('STRAND>')
reversed_strand = ''
reverse_compliment = ''

for i in range(len(strand)):
    reversed_strand += strand[-(i+1)]

#print(reversed_strand)

for i in range(len(reversed_strand)):
    if reversed_strand[i] == 'A':
        reverse_compliment += 'T'
    elif reversed_strand[i] == 'T':
        reverse_compliment +='A'
    elif reversed_strand[i] == 'C':
        reverse_compliment +='G'
    elif reversed_strand[i] == 'G':
        reverse_compliment +='C'
    else:
        print('invalid input')
        valid = False
        break

print('\nThe reverse compliment of that string is:')
print('OUTPUT',reverse_compliment)