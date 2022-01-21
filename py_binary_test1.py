#!/usr/bin/env python3
# 01.21.2022 15:58:08 CST
# title = python binary test
# description: input lucky number find this guy

my_number = [4, 11, 66, 87, 23, 9]

number_length = len(my_number) - 1
min = 0
max = number_length
find_count = 0
lucky_flag = False
# sorting the list before binary search 
for i in range(0, number_length):
    for j in range(0, number_length - i):
        if my_number[j] > my_number[j+1]:
            my_number[j], my_number[j+1] = my_number[j+1], my_number[j]
            
# type a lucky number
lucky_number = int(input("請輸入中奬號碼："))

# start binary search
while min <= max:
    mid = int((min+max)/2)
    find_count += 1
    if my_number[mid] == lucky_number:
        lucky_flag = True
        break
        
    if my_number[mid] > lucky_number:
        max = mid - 1
    else:
        min = mid + 1
        
if lucky_flag == True:
    print(f"找了 {find_count} 次")
    print(f"號碼 {lucky_number} 中奬了")
else:
    print(f"可惜號碼 {lucky_number} 沒有中奬")        
            
        
