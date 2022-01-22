#!/usr/bin/env python3
# 01.22.2022 12:31:14 CST
# title = about python search problems 1

# test 1
# type student grade: 78
# type student grade: 92
# type student grade: 53
# type student grade: 82
# type student grade: 45
# Before sort : [78, 92, 53, 82, 45]
# After sort (descening order) : [92, 82, 78, 53, 45]

student_grades = []
for i in range(5):
    grades = input("type student grade: ")
    student_grades.append(int(grades))
    
    
print(f"Before sort : {student_grades}")

st_len = len(student_grades)
for i in range(st_len):
    for j in range(i, st_len - 1):
        if student_grades[j] < student_grades[j+1]:
            student_grades[j], student_grades[j+1] = student_grades[j+1], student_grades[j]
            
print(f"After sort (descening order) : {student_grades}")
