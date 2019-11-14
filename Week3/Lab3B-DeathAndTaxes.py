#Brendan Uebelhoer
#CSCI 101- Section A
#Python Lab 3B

initial = 0.0
rem = 0.0
total = 0.0
percent = [.1, .15, .25, .28, .33, .35, .395]
bracket = 0

print('input filing status')
status = input('STATUS>')
initial = int(input('INCOME>'))
rem = initial

if status == 'single':
    cutoff = [9325, 28624, 53949, 99749, 225049, 1699]
elif status == 'joint':
    cutoff = [18650, 57246, 77199, 80249, 183349, 53999]
elif status == 'seperate':
    cutoff = [9325, 28625, 38599, 40124, 91674, 26999]
elif status == 'head':
    cutoff = [13350, 37449, 80399, 81299, 204199, 27799]
else:
    print('invalid input')
    initial = -1
    rem = 0
    total = 0

while bracket <= 5:
    if rem > cutoff[bracket]:
        total = total + percent[bracket] * cutoff[bracket]
        rem = rem - cutoff[bracket]
        bracket = bracket + 1
    else:
        total = total + percent[bracket] * rem
        rem = 0
        bracket = bracket + 1

if initial == -1:
    print('Error, unable to compute')
else:
    print('total amount paid in dollars:')
    print('OUTPUT:', int(total))

    total_percent = (total / initial) *100
    print('total percentage paid')
    print('OUTPUT',round(total_percent,2))
