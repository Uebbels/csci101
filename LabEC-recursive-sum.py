#Brendan Uebelhoer
#CSCI 101 section A
#Python Lab EC

def recursive_sum_odd(list,sum):
    if len(list) == 0:
        return 0
    if list[0] % 2 == 0:
        return sum + recursive_sum_odd(list[1:], 0)
    else:
        return sum + list[0] + recursive_sum_odd(list[1:],0)
