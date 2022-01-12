#!/usr/bin/env python3
# 01.12.2022 13:20:08 CST
# title = python_set2

countries_list = ['France', 'Taiwan', 'Japan', 'Italy', 'Austria', 'German']

country_set = set(countries_list)
print(type(country_set))

print('Austria' in countries_list)
print('Austria' in country_set)
print(country_set)

print("add a elements in a set: ")
country_set.add('India')
print(country_set)

# notice: set was not ordered
print("pop a element in a set: ")
country_set.pop()
print(country_set)

# Traceback (most recent call last):
  # File "python_set2.py", line 12, in <module>
    # country_set.append('India')
# AttributeError: 'set' object has no attribute 'append'

# country_set.append('India')



