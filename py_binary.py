#!/usr/bin/env python3
# 01.21.2022 15:05:40 CST
# title = python binary practice
# description: input lucky number find this guy

my_number = [128, 728, 987, 365, 178, 512, 803]
my_guy = ["Try哥", "阿J", "小美", "萬萬", "耗耗", "阿耗", "阿明"]

num_length = len(my_number) - 1
lucky_flag = False
min = 0
max = num_length
find_count = 0

for i in range(0, num_length):
    for j in range(0, num_length - i):
        if my_number[j] > my_number[j+1]:
            my_number[j], my_number[j+1] = my_number[j+1], my_number[j]
            my_guy[j], my_guy[j+1] = my_guy[j+1], my_guy[j]

print(my_number)
print(my_guy)
lucky_number = int(input("輸入中奬人的號碼："))

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
    print("This guy was : ", my_guy[mid])
else:
    print("No one got it.")

print("總共比對 %d 次" % (find_count))

