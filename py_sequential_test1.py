#!/usr/bin/env python3
# 01.21.2022 14:46:21 CST
# title =　python sequential test

my_number = [4, 11, 66, 87, 23, 9]

while True:
    lucky_number = input("輸入中奬的號碼：")
    if lucky_number == "":
        break

    myFlag = False
    for i in range(len(my_number)):
        if my_number[i] == int(lucky_number):
            myFlag = True
            break
            
    if myFlag == True:
        print(f"恭喜！號碼: {my_number[i]} 中奬")
    else:
        print(f"太可惜！號碼: {lucky_number} 未中奬")

