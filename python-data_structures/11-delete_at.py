#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list) or idx < 0 or len(my_list) == 0:
        return (my_list)
    my_list.remove(my_list[idx])
    return my_list
