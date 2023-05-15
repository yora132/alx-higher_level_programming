#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            return new_list = 1
        else:
            return new_list = 0
    return new_list
