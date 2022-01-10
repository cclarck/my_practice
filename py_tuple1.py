#!/usr/bin/env python3
# 01.10.2022 15:32:38 CST
# title = python tuple

today = 2022, 1, 10
year, month, day = today

# it was OK.
# year, month, day = 2022, 1, 10

print("Today is {}-{}-{}".format(year, month, day))

my_tuple_1 = 2, 4
my_tuple_2 = (2, 4)

print(my_tuple_1 == my_tuple_2)
print(my_tuple_1[0])
