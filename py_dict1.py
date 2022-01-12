#!/usr/bin/env python3
# 01.12.2022 13:43:48 CST
# title = python_dict1

# dictionary was ordered and unsort
my_dict = {'Tom': 10.9, 
        'Mary': 15.7, 
        'Abby': 19.2, 
        'Jack': 13.1}
print(my_dict)

# Traceback (most recent call last):
  # File "py_dict1.py", line 8, in <module>
    # print(my_dict['Peter'])
# KeyError: 'Peter'
# print(my_dict['Peter'])

# It was show None
print(my_dict.get('Peter'))
print(my_dict.get('阿明', 'No this guy here!'))

# a and b are the same object, c is other object
a = [3, 2, 1]
b = a
c = [3, 2, 1]

print(a == b)
print(a is b)
print(a == c)
print(a is c)
print(b == c)
print(b is c)
