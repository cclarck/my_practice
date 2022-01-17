#!/usr/bin/env python3
# 01.17.2022 14:55:54 CST
# title = python iterable 2

# test2
# test2
# thinking 1 ...
# [0]
# [0, 1]
# [0, 1, 2]
# [0, 1, 2, 3]
# [4]
# [4, 5]
# [4, 5, 6]
# [4, 5, 6, 7]
# ...
# [24, 25, 26]
# def my_number_group(iterable, size):
    # my_list = []
    # for i in iterable:
        # if len(my_list) < size:
            # my_list.append(i)
        # else:
            # my_list = []
            # my_list.append(i)
        # yield  my_list

# for number_group in my_number_group(range(27), 4):
    # print(list(number_group))

# thinking 2 ...
# result was same as thinking 1 ...
# def my_number_group(iterable, size):
    # my_list = []
    # for i in iterable:
        # my_list.append(i)
        # if len(my_list) > size:
            # my_list = []
            # my_list.append(i)
        # yield  my_list

# for number_group in my_number_group(range(27), 4):
    # print(list(number_group))
    
# thinking 3 ...
# this right result
# [0, 1, 2, 3]
# [4, 5, 6, 7]
# [8, 9, 10, 11]
# [12, 13, 14, 15]
# [16, 17, 18, 19]
# [20, 21, 22, 23]
# [24]

def my_number_group(iterable, size):
    """yield the iterable length of size"""
    for i in range(0, len(iterable), size):
        yield iterable[i:i+size]

for number_group in my_number_group(range(27), 4):
    print(list(number_group))
