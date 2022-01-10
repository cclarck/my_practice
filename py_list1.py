#!/usr/bin/env python3
# 01.10.2022 13:18:45 CST
# title = python list
# list is mutable and ordered

months = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', \
            '八月', '九月', '十月', '十一月', '十二月']
            
print(months)
# index
print(months[0])
print(months[2])
print(months[9])
print(months[-1])
print(months[-2])

# slice
q2 = months[3:6]
print(q2)
second_half = months[-6:]
print(second_half)

# how long list
print(len(months))
print('星期日' in months, '星期日' not in months)

# Traceback (most recent call last):
  # File "py_list1.py", line 13, in <module>
    # print(months[99])
# IndexError: list index out of range
# print(months[99])

my_list = [9, 1.2, False, '哈囉']
print(my_list)
print(my_list[0])
print(my_list[len(my_list) - 1])
print(my_list[-2])
print(my_list[:2])
print(my_list[1:])

months[1] = '星期二'
print(months)
