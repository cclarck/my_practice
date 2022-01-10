#!/usr/bin/env python3
# 01.10.2022 14:28:04 CST
# title = list methonds

scores = ["B", "D", "A", "C", "B", "A"]
grades = scores

# Traceback (most recent call last):
  # File "py_list2.py", line 7, in <module>
    # print("scores: " + scores)
# TypeError: can only concatenate str (not "list") to str

print("scores: " + str(scores))
print("grades: " + str(grades))
scores[3] = "B"
print("scores: " + str(scores))
print("grades: " + str(grades))

pythons = ['Ball Python', 'Burmese Python', 'African Rock Python', 
'Reticulated Python', 'Angolan Python']

# max methond
print(max(pythons))
print(min(pythons))

# sorted methond
sizes = [87, 5, 11, 27, 66, 45]
print(sorted(sizes))
print(sorted(sizes, reverse=True))
print(max(sizes))
print(min(sizes))

# join methond
my_programs = "\n".join(["rust", "julia", "python", "shell script"])
print(my_programs)

places = ["Collège Royal" "Henry" "Le" "Grand"]
print("-".join(places))

something = ["a", 33, "c"]

# Traceback (most recent call last):
  # File "py_list2.py", line 41, in <module>
    # print(" and ".join(something))
# TypeError: sequence item 1: expected str instance, int found
# print(" and ".join(something))

letters = ['a', 'b', 'f', 'd']
letters.append('g')
print(letters)

a = [1,2,3]
b = [4,5,6]
print(a.append(b))
#result_1 = a.append(b)
print(a+b)
# result_2 = a + b
# print(result_1)
# print(type(result_1))
# print(result_2)
# print(type(result_2))
