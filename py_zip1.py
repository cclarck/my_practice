#!/usr/bin/env python3
# 01.14.2022 16:35:52 CST
# title = python zip 1

# pizza topping practice
toppings = ['Pepperoni', 'Hawaiian', 'BBQ chicken', 'Double cheese', 'Neapolitan']
price = [20, 15, 30, 40, 50, 55]

print(list(zip(toppings, price)))

menu = [('Pepperoni', 20), ('Hawaiian', 15), ('BBQ chicken', 30), ('Double cheese', 40), ('Neapolitan', 50)]

foods, pizza_price = zip(*menu)

print(foods)
print(pizza_price)

print("test1 combine points: ")
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []

# mode 1
for label, x, y, z in zip(labels, x_coord, y_coord, z_coord):
    print("{}: {}, {}, {}".format(label, x, y, z))
    points.append(label+": "+ str(x) + ", " + str(y) + ", "+ str(z))

# mode 2
# for point in zip(labels, x_coord, y_coord, z_coord):
    # points.append("{}: {}, {}, {}".format(*point))
    
for point in points:
    print(point)

print("test2 packing: ")
dogs_names = ["Jimmmy", "Kuro", "Momo", "Tom", "Jelly"]
dogs_weights =  [20, 17, 10, 13, 5]

dogs = dict(zip(dogs_names, dogs_weights))
print(dogs)

print("test3 unpacking: ")
dogs = (('Jimmmy', 60), ('Kuro', 77), ('Momo', 65), ('Tom', 50), ('Jelly', 30))
names, heights = zip(*dogs)

print(names)
print(heights)

print("test4 matrix transpose: ")
print(list(zip('ABCD', 'xy')))
my_tuple = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

print(len(my_tuple))
tuple_transpose = tuple(zip(*my_tuple))
print(len(tuple_transpose))
print(tuple_transpose)
