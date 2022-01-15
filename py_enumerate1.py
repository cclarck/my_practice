#!/usr/bin/env python3
# 01.15.2022 12:40:11 CST
# title = python enumerate vs zip

toppings = ['Pepperoni', 'Hawaiian', 'BBQ chicken', 'Double cheese', 'Neapolitan']

# using enumerate
print("enumerate:")
for i, topping in enumerate(toppings):
    print(i, topping)

# using zip
print("zip:")
for i, topping in zip(range(len(toppings)), toppings):
    print(i, topping)

print("test1 combine: ")
persons = ["阿明", "小美", "阿How", "HowFun", "RJ"]
heights = [100, 168, 172, 180, 176]

for i, person in enumerate(persons):
    persons[i] = person + " " + str(heights[i])
    
print(persons)
