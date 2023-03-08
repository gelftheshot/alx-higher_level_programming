#!/usr/bin/python3
# 10-best_score.py

def best_score(a_dictionary):

    if not isinstance(a_dictionary, dict) or len(a_dictinary) == 0:
        return None

    key = list(a_dictionary.keys())[0]
    max1 = a_dictionary[key]

    for i, j in a_dictionary.items():
        if j > max1:
            max1 = j
            key = i
    return (key) 
