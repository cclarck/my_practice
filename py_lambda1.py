#!/usr/bin/env python3
# 01.16.2022 17:11:35 CST
# title =　python lambda 1

# practice 1
x2 = lambda x: x * 2
print(x2(10))

# test1
my_lists = [
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8, 10],
        [1, 3, 5, 7, 9],
        [5, 10, 15, 20, 25],
    ]

# method 1: 
# def my_mean(number_list):
    # """Caculate each lists' number average."""
    # return sum(number_list) / len(number_list)
    
# list_avg = list(map(my_mean, my_lists))
# print(list_avg)    

# method 2: using lambda    
list_avg = list(map(lambda x: sum(x)/len(x), my_lists))
print(list_avg)


# test2
tw_cities = ['pingtung', 'hsinchu', 'taichung', 'tainan', 'kaohsiung', 'taoyuan']

# method 1: 
# def long_length_city(cities):
    # """Finding city name length > 7"""
    # return len(cities) > 7 

# long_length_cities = list(filter(long_length_city, tw_cities))
# print(long_length_cities)

# method 2: using lambda
long_length_cities = list(filter(lambda x: len(x) >7, tw_cities))
print(long_length_cities)




