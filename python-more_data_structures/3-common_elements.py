#!/usr/bin/python3
def common_elements(set_1, set_2):
    s = ()
    set2 = list(set_2)
    for i in set_1:
        if set2.count(i) > 0:
            s = s + (i,)
    return s
