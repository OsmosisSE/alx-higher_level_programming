#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = set(my_list)
    add_num = 0

    for a in new_list:
        add_num += a

    return (add_num)
