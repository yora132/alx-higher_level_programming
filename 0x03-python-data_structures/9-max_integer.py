#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    big = my_list[0]
    for i in range(1, len(my_list)):
        if big < my_list[i]:
            big = my_list[i]
        else:
            continue
    return big
