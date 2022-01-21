#!/usr/bin/env python3
# 01.21.2022 14:31:53 CST
# title = python sequential practice
# description: input lucky number find this guy

my_number = [128, 728, 987, 365, 178, 512, 803]
my_guy = ["Try哥", "阿J", "小美", "萬萬", "耗耗", "阿耗", "阿明"]

lucky_number = int(input("輸入中奬人的號碼："))
lucky_flag = False

for i in range(len(my_guy)):
    if (my_number[i] == lucky_number):
        lucky_flag = True
        break
        
if (lucky_flag == True):
    print(i)
    print("This guy was : ", my_guy[i])
else:
    print("No one got it.")

print("總共比對 %d 次" % (i+1))
