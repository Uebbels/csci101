#Brendan Uebelhoer
#CSCI 101-Section A
#Python Lab 9

def Multiply(a,b,c):
    if a * b == c: return True
    else: return False

def BoundsChecking(a,b,c):
    if a >= 0 and b <= (c - 1) and a < b: return True
    else: return False

def DecimalPoints(a):
    b = str(a).split('.')
    if len(b[1]) == 3: return True
    else: return False

def ListSorted(a):
    is_sorted = False
    if a == sorted(a):
        is_sorted = True
    return is_sorted

def ReversedList(a,b):
    reversed = True
    for i in range(len(a)):
        if a[i] != b[-(i + 1)]:
            reversed = False
    return reversed

def NumZeros(n,a):
    counter  = 0
    for i in a:
        for j in i:
            if j == ('o' or 'O'):
                counter += 1
    if counter == n:
        return True
    else:
        return False

def CheckCS(a):
    containsC = False
    containsS = False
    for i in a:
        if i == 'c':
            containsC = True
        elif containsC:
            if i == 's':
                containsS = True
    return containsS