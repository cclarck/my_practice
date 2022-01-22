#!/usr/bin/env python3
# 01.22.2022 13:33:03 CST
# title = about python search problems 2

# test 2
# Please type the 1 number :12
# Please type the 2 number :3
# Please type the 3 number :5
# Congrat! You got 2 numbers.

num = [67, 12, 9, 52, 91, 3]
lucky_num = []
my_count = 0
for i in range(3):
    input_no = input("Please type the " + str(i+1) + " number :")
    lucky_num.append(int(input_no))

# method 1
# for i in range(0,3):    
    # for j in range(len(num)):
        # if (lucky_num[i] == num[j]):
            # my_count += 1
            # break

# method 2
for i in range(3):
    if lucky_num[i] in num:
        my_count += 1
        
if my_count <= 0:
    print("So bad...")
else:
    print(f"Congrat! You got {my_count} numbers.")
