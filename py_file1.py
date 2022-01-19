#!/usr/bin/env python3
# 01.19.2022 13:13:45 CST
# title = python read and write 1

print("read file method 1:")
f = open('my_file220119.txt', 'r')
file_read = f.read()
f.close()

print(file_read)

print("read file method 2:")
with open('my_file220119.txt', 'r') as f:
    file_content = f.read()
    
print(file_content)

print("read file test 1: with and read()")
with open('my_file220119.txt') as intro:
    print(intro.read(1))
    print(intro.read(10))
    print(intro.read())
    
    
print("read file test 2: readline()")
start_intro = []
with open('my_file220119.txt') as intro:
    for line in intro:
        start_intro.append(line.strip())

print(start_intro)

# write
f = open('my_other_file220119.txt', 'w')
f.write('Hello, how do you do? ')
f.close()

