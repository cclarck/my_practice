#!/usr/bin/env python3
# 01.19.2022 13:47:12 CST
# title = python read and write 2

# practice 1
# result: 
# ['Graham Chapman', '  Various / ... (46 episodes', ' 1969-1974)\n']
# ['Eric Idle', '  Various / ... (46 episodes', ' 1969-1974)\n']
# ...
# ['Suzy Mandel', '  German Girl (uncredited) (1 episode', ' 1974)\n']
# ['Peter Woods', '  BBC Presenter (uncredited) (1 episode', ' 1974)']

def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open('flying_circus_cast.txt') as f:
        #use the for loop syntax to process each line
        for cast in f:
            cast_line = cast.split(",")
            #and add the actor name to cast_list
            cast_list.append(cast_line)

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
