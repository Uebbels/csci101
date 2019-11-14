#Brendan Uebelhoer
#CSCI 102 Section c
#Week 11 Part A
import string
import random

def clean_word(in_string):
    print(in_string,end=' ')
    string_list = []
    for i in in_string:
        if i in string.punctuation:
            continue
        elif i == (' ' or '\n'):
            continue
        else:
            string_list.append(i.lower())
    out_string = ''.join(string_list)
    print(out_string)
    return out_string

def read_file(path):
    with open(path,'r') as file:
        out_string = file.read()
    out_list = out_string.split()
    return out_list

def write_file(list,output,length,seed):
    random.seed(seed)
    out_list = []
    while length > 0:
        out_list.append(clean_word(list[random.randint(0,len(list)-1)]))
        length -= 1
    out_string = ' '.join(out_list)
    print(out_string)
    with open(output,'w') as out_file:
        out_file.write(out_string)