#!/usr/bin/env python3
# 01.16.2022 12:45:24 CST
# title = python comprehension 2

# test1 get city and lowercase city
tw_cities = ['Taipei city', 'Hsinchu city', 'Taichung city', 'Tainan City']
print(tw_cities)
# method 1
# for tw_city in tw_cities:
    # tw_city = tw_city.split()[0].lower()
    # print(tw_city)

# method 2
lower_tw_cities = [tw_city.split()[0].lower() for tw_city in tw_cities]
print(lower_tw_cities)

# test2 multiple 11
x11 = [i*11 for i in list(range(1, 11))]
print(x11) 

# test3 name with height filter >= 160
print("test3 filter height over 160: ")
persons = {"阿明": 189, "小美": 159, "阿How": 161, "FunHow": 171, "R借": 180}

# method 1
# for name, height in persons.items():
    # if height >= 65:
        # print(f'名字: {name}, 身高: {height}')

# method 2
height_checked = [name for name, score in persons.items() if score >= 160]
print(height_checked)
