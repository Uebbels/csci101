#Brendan Uebelhoer
#CSCI 102 - Section C
#Week 3 - Part C

acid = ' '

print('Please input the chemical composition of the amino acid\n')
carbon = int(input('CARBON>'))
hydrogen = int(input('HYDROGEN>'))
nitrogen = int(input('NITROGEN>'))
oxygen = int(input('OXYGEN>'))
sulfur = int(input('SULFUR>'))

if hydrogen == 7:
    if sulfur == 1:
        acid = 'Cysteine'
    elif sulfur == 0:
        acid = 'Alanine'
    else:
        acid = 'unknown'
elif hydrogen == 8:
    acid = 'Asparagine'
elif hydrogen == 9:
    acid = 'Histidine'
elif hydrogen == 10:
    acid = 'Glutamine'
elif hydrogen == 14:
    acid = 'Arginine'
else:
    acid = 'unknown'

print('\nOUTPUT', acid) 
