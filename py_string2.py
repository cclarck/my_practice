#!/usr/bin/env python3
# 01.10.2022 12:36:56 CST
# title = python string 2
# sting is immutable and ordered

print(type(123))
print(type("5566"))
print(type(55.66))
print(type(False))

print("hello world".title())
greeting = "hello world"
# how long string
print(len(greeting))
# slice
print(greeting[6:9])
# index
print(greeting[4])
print(greeting.islower())
print(greeting.count('l'))
print(greeting.find('l'))

# Traceback (most recent call last):
  # File "py_string2.py", line 21, in <module>
    # greeting[1] = 'x'
# TypeError: 'str' object does not support item assignment
# greeting[1] = 'x'
# print(greeting[1])

print("一隻魚，兩隻魚，三隻魚，黃魚".count('魚'))
