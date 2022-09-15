#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    m1 = 0
    m2 = ''
    for i in a_dictionary:
        if a_dictionary[i] > m1:
            m1 = a_dictionary[i]
            m2 = i
    return m2
