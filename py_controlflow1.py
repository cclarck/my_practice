#!/usr/bin/env python3
# 01.13.2022 12:51:40 CST
# title = python control flow 1

season = 'fall'

if season == 'spring':
    print('三月到五月')
elif season == 'summer':
    print('六月到八月')
elif season == 'fall':
    print('九月到十一月')    
elif season == 'winter':
    print('十二月到二月')
else:
    print('沒這季節！')

my_points = 201  

if my_points <= 0:
    result = "Invalid score."
if my_points <= 100:
    result = "Congratulations! You won a apple!"
elif my_points <= 150:
    result = "Congratulations! You won a banana!"
elif my_points <= 200:
    result = "Congratulations! You won a beef!"
elif my_points <= 250:
    result = "Congratulations! You won a fish!"
else:
    result = "Invalid score."
    
print(result)

# true or false
points = 188
prize = None

if points <= 100:
    prize = "apple"
elif points <= 150:
    prize = "banana"
elif points >= 200:
    prize = "fish"

if prize:
    result = "Congratulations! You won a " + prize + "!"
else:
    result = "Nothing."
    
print(result)
