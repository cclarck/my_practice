#!/usr/bin/env python3
# 01.19.2022 14:05:33 CST
# title = python read and write 2 v1

# result: 
# Graham Chapman
# Eric Idle
# Terry Jones
# ...
# Suzy Mandel
# Peter Woods

def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open('flying_circus_cast.txt') as f:
        #use the for loop syntax to process each line
        for cast in f:
            cast_line = cast.split(",")
            #and add the actor name to cast_list
            cast_list.append(cast_line[0])

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
