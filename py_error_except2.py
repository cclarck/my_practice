#!/usr/bin/env python3
# 01.19.2022 12:47:03 CST
# title = python error except 2

# test 1
# modify the except ...
# before:
# def create_groups(items, num_groups):
    # size = len(items) // num_groups

    # groups = []
    # for i in range(0, len(items), size):
        # groups.append(items[i:i + size])

    # print("{} groups returned.".format(num_groups))
    # return groups

# print("Creating 6 groups...")
# for group in create_groups(range(32), 6):
    # print(list(group))

# print("\nCreating 0 groups...")
# for group in create_groups(range(32), 0):
    # print(list(group))
    
# after:
# not right ...
# def create_groups(items, num_groups):
    # try:
        # size = len(items) // num_groups
        # groups = []
        # for i in range(0, len(items), size):
            # groups.append(items[i:i + size])

        # print("{} groups returned.".format(num_groups))
        # return groups
    # except ZeroDivisionError:
        # groups = []
        # print("WARNING: Returning empty list. Please use a nonzero number.")
        # print("{} groups returned.".format(num_groups))
        # return groups
        

# print("Creating 6 groups...")
# for group in create_groups(range(32), 6):
    # print(list(group))

# print("\nCreating 0 groups...")
# for group in create_groups(range(32), 0):
    # print(list(group))

# the good 
def create_groups(items, num_groups):
    try:
        size = len(items) // num_groups
    except ZeroDivisionError:
        print("WARNING: Returning empty list. Please use a nonzero number.")
        return []
    else:
        groups = []
        for i in range(0, len(items), size):
            groups.append(items[i:i + size])
        return groups
    finally:
        print("{} groups returned.".format(num_groups))
    
print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))   
