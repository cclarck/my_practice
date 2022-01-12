#!/usr/bin/env python3
# 01.12.2022 13:34:20 CST
# title = python_set3

a = [1, 1, 2, 3, 3, 3, 3, 4, 4, 4]
b = set(a)

# notice: the result was amazing!
print(len(a)) 
print(len(b)) # unique element from a set
print(len(a) - len(b))

# in python_set2, you could see the same result!
# pop in set was not removed last one 
a = [1, 2, 2, 2, 2, 3, 3, 4, 4, 4]
b = set(a)
b.add(6)
print(b)
b.pop()
print(b)
