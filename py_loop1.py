#!/usr/bin/env python3
# 01.14.2022 12:53:29 CST
# title = python loop: for

tw_cities = ['taipei', 'hsinchu', 'taichung', 'tainan']
title_tw_cities = []
upper_tw_cities = []

print(tw_cities)
for tw_city in tw_cities:
    print(tw_city.title())
    
for tw_city in tw_cities:
    title_tw_cities.append(tw_city.title())
    
print(title_tw_cities)

for i in range(len(title_tw_cities)):
    title_tw_cities[i] = title_tw_cities[i].upper()
    
print(title_tw_cities)
    
# range
print(range(4))
print(list(range(4)))
print(list(range(1, 4)))
print(list(range(2, 10, 2)))

# for example
tags = ['<p>', 'Hello World!', '</p>']

count = 0
for tag in tags:
    if tag[0] == '<' and tag[-1] == '>':
        count += 1

print(count)

items = ['about', 'category']
html_str = "<ul>\n" 
for i in range(len(items)):
    # html_str = html_str + "<li>" + items[i] + "</li>\n"
    html_str = html_str + "<li>{}</li>\n".format(i)
        
html_str = html_str + "</ul>"
print(html_str)
