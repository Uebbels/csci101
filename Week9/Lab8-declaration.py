#Brendan Uebelhoer
#CSCI 101 -Section A
#Python Lab 8

import random
import string
from string import punctuation

function = 0
counter = 0
function = int(input('Would you like to print the number of times a specific word appears OR print the number of words of a specific length? (1 or 2)\nCHOICE>'))

with open('Declaration_of_independence.txt','r') as f:
    declaration = f.read()

if function == 1:
    word = input('WORD>')
    word = word.lower()
    for i in range(len(declaration)):
        if declaration[i:i+len(word)].lower() == word:
            counter += 1
    print('OUTPUT %d' % counter)        


elif function == 2:
    punctuation = ['.',',',':',';','[',']','(',')','"',"'",'—'] 
    length = int(input('LENGTH>'))
    words = []
    edited_declaration = []
    for i in declaration:
        if i in punctuation:
            edited_declaration.append(' ')
        else:
            edited_declaration.append(i)
    edited_declaration = ''.join(edited_declaration)        
    edited_declaration = edited_declaration.split()
    for i in edited_declaration:
        if len(i) == length:
            counter += 1
            words.append(i)        
    print('OUTPUT %d' % counter)
    print('OUTPUT',words[random.randint(0,len(words)-1)])

