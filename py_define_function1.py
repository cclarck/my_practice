#!/usr/bin/env python3
# 01.16.2022 13:57:43 CST
# title =　python define function by yourself 1

# practice 1
print("cube volume: ")
def cube_volume(height, square=10):
    return height * square ** 2

# notice: arguments postion    
print(cube_volume(10, 17))
print(cube_volume(10, 10))
print(cube_volume(height=10, square=10))
print(cube_volume(5, square=10)) 
# print(cube_volume(11, height=5))
# print(cube_volume(square=5, height=5))
print(cube_volume(10))

# practice 2
print("How many minutes and seconds? ")
def readable_timedelta(seconds):
    """Print the number of minutes and seconds in a number of seconds."""
    mins = seconds // 60
    secs = seconds % 60
    return "{} minute(s) and {} second(s).".format(mins, secs)
    
print(readable_timedelta(61))

# scope: integer, string
print("scope test: ")
beer_count = 0

def buy_beer(count):
    return count + 12

beer_count = buy_beer(beer_count)
print(f"beer: {beer_count}")

# UnboundLocalError: local variable 'beer_count' referenced before assignment
# beer_count = 0
# def buy_beer():
    # beer_count += 12

# buy_beer()

# docstring example
def cube_volume(height, square):
    """計算立方體體積
    輸入：
    height: int or float. 高度
    square: int or float.　面積單位需自行計算，如果是長方體不是立方體。
    
    輸出：
    height * square ** 2　想要計算的立方體體積
    """
    return height * square ** 2
