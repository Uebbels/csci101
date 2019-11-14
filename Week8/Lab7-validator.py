#Brendan Uebelhoer
#CSCI 101 Section A
#Python LAb 7

import random

my_seed = int(input("Number to initialize the random generator: "))
random.seed( my_seed )

password_score = 0
operation = 0
lowercase_count = 0
uppercase_count = 0
password = ''
password_rank = ''
password_state = False
contains_number = False
contains_symbols = False
long_enough = False
special_charaters = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','[','{',']','}','|',';',':','\\','"',"'",'<','>','?','/',',']
vowels = ['a','e','i','o','u','A','E','I','O','U']

operation = int(input('Would you like to 1) evaluate an inputed password or 2) randomly generate a password\nCHOICE>'))

if operation == 1:
    password = input('PASSWORD>')
    print('Validating ')
    if len(password) >= 8:
        long_enough = True
    for i in password:
        if i.isdecimal() == True:
            contains_number = True
        if i in special_charaters:
            contains_symbols = True

    if long_enough and contains_number and contains_symbols == True:
        password_state = True



elif operation == 2:
    password_list = ['a','a','a','a','a','a','a','a',0,0,'-','-']
    for  i in range(8):
        if random.randint(0,1) == 0:
            password_list[i] = chr(random.randint(65,90))
        else:
            password_list[i] = chr(random.randint(97,122))
    password_list[8] = str(random.randint(0,9))
    password_list[9] = str(random.randint(0,9))
    password_list[10] = special_charaters[random.randint(0,len(special_charaters))]
    password_list[11] = special_charaters[random.randint(0,len(special_charaters))]
    password = ''.join(password_list)
    password_state = True

if password_state == True:
    print('Password validated')
    for i in password:
        if i.islower() == True:
            password_score += 4
            lowercase_count += 1
        if i.isupper():
            password_score += 4
            uppercase_count += 1
        if i.isdigit() == True:
            password_score += 5
        if i in special_charaters:
            password_score += 6
        if i in vowels:
            password_score -= 3
    password_score += (uppercase_count - lowercase_count) * 2
        
    if password_score < 20:
        password_rank = 'Weak+'
    elif password_score < 40:
        password_rank = 'Weak'
    elif password_score < 60:
        password_rank = 'Good'
    elif password_score < 80:
        password_rank = 'Strong'
    else:
        password_rank = 'Strong+'
    print('The password %s is a %s password' %(password, password_rank))
    print('OUTPUT',password_rank)
    
else:
    print('Password invalid, please try again\nOUTPUT INVALID')
