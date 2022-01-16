#!/usr/bin/env python3
# 01.15.2022 16:07:57 CST
# title = python list comprehensions

print("list comprehension 1: ")
tw_cities = ['taipei', 'hsinchu', 'taichung', 'tainan']
title_tw_cities = [tw_city.title() for tw_city in tw_cities]
print(title_tw_cities)

upper_tw_cities = [tw_city.upper() for tw_city in tw_cities]
print(upper_tw_cities)

print("list comprehension 2: ")
my_squares = [x**2 for x in range(10)]
print(my_squares)

print("adding if: ")
my_squares2 = [x**2 for x in range(10) if x % 2 == 0]
print(my_squares2)

print("adding if else: ")
my_squares3 = [x**2 if x % 2 == 0 else x + 5 for x in range(10)]
print(my_squares3)


print("list No comprehension 2: ")
normal_squares = []
for x in range(10):
    normal_squares.append(x ** 2)
print(normal_squares)

