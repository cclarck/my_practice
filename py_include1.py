#!/usr/bin/env python3
# 01.19.2022 14:25:59 CST
# title = python include python script 1

# test 1
import my_function as myf

num = [1, 3, 5, 8, 9]

mean = myf.mean_result(num)
add_num = myf.add_three(num)

print("number: ", num)
print("number mean: ", mean, " add number: ", add_num)

print(__name__)
print(myf.__name__)
