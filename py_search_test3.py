#!/usr/bin/env python3
# 01.22.2022 14:29:51 CST
# title = # title = about python search problems 3

# result:
# 輸入中奬者：阿J
# Congrat! 阿J got it!
# 輸入中奬者：JJ  
# So bad ...

names = ["阿明", "耗哥", "Try哥", "阿J", "小美", "耗放"]
names_len = len(names) - 1

# setup 1: sort 
for i in range(0, names_len):
    for j in range(0, names_len - i):
        if names[j] > names[j+1]:
            names[j], names[j+1] = names[j+1], names[j]
            
print(names)

# setup 2: search
    
while True:
    lucky_guy = input("輸入中奬者：(輸入Exit結束)")
    if lucky_guy == "Exit":
        break
        
    my_flag = False
    min = 0
    max = names_len
 
    while min <= max:
        mid = int((min+max)/2)
        if names[mid] == lucky_guy:
            my_flag = True
            break
            
        if names[mid] > lucky_guy:
            max = mid - 1
        else:
            min = mid + 1
    
    if my_flag == True:
        print(f"Congrat! {names[mid]} got it!")
    else:
        print(f"So bad ...")
    
