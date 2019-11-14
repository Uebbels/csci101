#Brendan Uebelhoer
#CSCI 101 Section A
#Python lab 3A
print('what would you like to decode?')
tweet = input('TWEET>')
print('\nThat abbreviation is')
print('OUTPUT', end=' ')
if tweet == 'LOL':  #borrowed code from zybook
    print('LOL = laughing out loud')
elif tweet == 'BFN':
    print('BFN = bye for now')
elif tweet == 'FTW':
    print('FTW = for the win')
elif tweet == 'IRL':
    print('IRL = in real life') #end borrowed code
elif tweet == 'BTW':
    print('BTW = by the way')
elif tweet == 'CU':
    print('CU = see you')
elif tweet == 'AFAIK':
    print('AFAIK = as far as I know')
elif tweet == 'IDK':
    print('IDK = I dont know')
else:
    print("Sorry, don't know that one") #borrowed code from zybook
