#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    list_tup = []

    for i in range(2):
        if len(tuple_a) == 0:
            return (tuple_b)
        if len(tuple_b) == 0:
            return (tuple_a)
        if len(tuple_a) == 1:
            list_tup.append(tuple_a[i] + tuple_b[i])
            list_tup.append(tuple_b[i+1])
            return (tuple(list_tup))
        if len(tuple_b) == 1:
            list_tup.append(tuple_a[i] + tuple_b[i])
            list_tup.append(tuple_a[i+1])
            return (tuple(list_tup))
        list_tup.append(tuple_a[i] + tuple_b[i])
    return (tuple(list_tup))
