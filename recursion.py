def recursive_sum_odd(list,sum):
    if len(list) == 0:
        return 0
    elif list[1] % 2 == 0:
            evenlist.append(list[1])
        list.remove(list[1])
        return evenlist + filtereven(list)
    else:
        return 