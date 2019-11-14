#Brendan Uebelhoer
#CSCI 101 Section A
#Python Lab 4

guesses = 0
characters_used = []
secret_word = ' '
word_lenght = 0
char = ' '
guessed = False

secret_word = input('WORD>')
word_length = len(secret_word)
guesses = int(input('NUM>'))

while guesses > 0 and guessed == False:
    print('\n\nplease input a character(type "exit" to exit):')
    char = input('CHAR>')
    guesses -= 1
    if len(char) == 1:
        if char in secret_word:
            print('OUTPUT Sucess, you have guessed a character in the word!')
        else:
            print('OUTPUT Boo! You guessed incorrectly')
        characters_used.extend([char])
        
    else:
        if char == secret_word:
            guessed = True
        elif char == 'exit':
            break
        else:
            print('Sorry, that is not the word')


    if guesses > 0:
        print('%d guesses remaining' % guesses)
    
    print('You have guessed',characters_used)
    print('OUTPUT secret word', end=' ')

    for x in secret_word:
        if x in characters_used:
            print(x, end=' ')
        else:
            print('_', end = ' ')

if guessed == True:
    print('\nOUTPUT You have successfully guessed the word %s!' % secret_word)
else:
    print('\nOUTPUT Sorry, you have run out of guesses')
    print('OUTPUT Secret word was', secret_word)

