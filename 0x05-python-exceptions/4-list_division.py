#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            new_ele = my_list_1[i] / my_list_2[i]
        except IndexError:
            new_ele = 0
            print("out of range")
        except ZeroDivisionError:
            new_ele = 0
            print("division by 0")
        except TypeError:
            new_ele = 0
            print("wrong type")
        finally:
            new_list.append(new_ele)
    return new_list
