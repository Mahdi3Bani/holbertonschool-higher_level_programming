#!/usr/bin/python
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return
    print("element at indexElement at index {:d} is {:d} ".format(
        idx, my_list[idx]))
