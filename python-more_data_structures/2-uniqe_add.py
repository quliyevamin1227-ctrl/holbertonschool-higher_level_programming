#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    unique = []

    for number in my_list:
        if number not in unique:
            unique.append(number)
            total += number

    return total
