#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    s = ()
    set2 = list(set_2)
    set1 = list(set_1)
    for i in set_1:
        if set2.count(i) == 0:
            s = s + (i,)
    for i in set_2:
        if set1.count(i) == 0:
            s = s + (i,)
    return s
