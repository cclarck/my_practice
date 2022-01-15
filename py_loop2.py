#!/usr/bin/env python3
# 01.14.2022 13:58:30 CST
# title = python loop while and loop problem

# max int * int < num
num = 48

i = 0
while (i+1)**2 < num:
    i += 1
    i_square = i**2
    
print(i_square)

# max text length 154
newslines = ["Lorem ipsum dolor sit amet",
             "admodum recteque vituperatoribus has ad",
             "aeque argumentum mei ut. Vis elit etiam no",
             "Appareat gubergren dissentias ex his",
             "Cum enim aperiam alienum ei",
             "Papperbok Review: Totally Triffic"]

news_title = ""
news_title_length = 0
for newsline in newslines:
    news_title = news_title + newsline + " "
    if len(news_title) >= 154:
        news_title = news_title[:154]
        break
        
print("Final lenght: " + str(len(news_title)))
print(news_title)
