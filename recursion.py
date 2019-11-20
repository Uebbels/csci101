def recursive_sum_odd(list,sum):
    if len(list) == 0:
        return 0
    if list[0] % 2 == 0:
        print('debug 1',sum)
        return sum + recursive_sum_odd(list[1:], 0)
    else:
        print('debug 2',sum )
        return sum + list[0] + recursive_sum_odd(list[1:],0)
