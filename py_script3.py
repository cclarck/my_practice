#!/usr/bin/env python3
# 01.18.2022 16:06:43 CST
# title = python script 3

# output
# 輸入學生名字，用逗號分隔：Mary,Joy,Tom,Adam
# 輸入繳交作業次數，用逗號分隔：3,6,0,2
# 輸入作業成績，用逗號分隔：81,77,92,88
# Hi! Mary 提醒通知你己經繳交 3 在畢業之前，目前你的成績為 81，在截止前補交所有作業，成績會加到 87
# Hi! Joy 提醒通知你己經繳交 6 在畢業之前，目前你的成績為 77，在截止前補交所有作業，成績會加到 89
# Hi! Tom 提醒通知你己經繳交 0 在畢業之前，目前你的成績為 92，在截止前補交所有作業，成績會加到 92
# Hi! Adam 提醒通知你己經繳交 2 在畢業之前，目前你的成績為 88，在截止前補交所有作業，成績會加到 92


# method 1:  
student_names = input("輸入學生名字，用逗號分隔：")
student_assignments = input("輸入繳交作業次數，用逗號分隔：")
student_grades = input("輸入作業成績，用逗號分隔：")

# my try 1
# for name in student_names.split(","):
    # print(name)

# my try 2
# for name, assignment, grade in student_names, student_assignments, student_grades:
    # #print(i)

# my try 3
# for i in zip(student_names.split(","), student_assignments.split(","), student_grades.split(",")):
    # print(i[0], i[1], i[2])
      
for name, assignment, grade in zip(student_names.split(","), student_assignments.split(","), student_grades.split(",")):    
    print(f"Hi! {name.title()} 提醒通知你己經繳交 {assignment} 在畢業之前，\
    目前你的成績為 {grade}，在截止前補交所有作業，成績會加到 {int(grade) + int(assignment) * 2}")

# method 2:
# student_names = input("輸入學生名字，用逗號分隔：").title().split(",")
# student_assignments = input("輸入繳交作業次數，用逗號分隔：").split(",")
# student_grades = input("輸入作業成績，用逗號分隔：").split(",")

# msg = "Hi {} 提醒通知你己經繳交 {} 在畢業之前，目前你的成績為 {}，在截止前補交所有作業，成績會加到 {}"

# for name, assignment, grade in zip(student_names, student_assignments, student_grades):
    # print(msg.format(name, assignment, grade, int(grade) + int(assignment)*2))
