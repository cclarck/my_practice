#!/usr/bin/env python3
# 01.18.2022 15:37:36 CST
# title = python script 2

# practice 1
my_output = eval(input("輸入表達示: "))
print(my_output)

# test2:
# 輸入表達示: 你好
# Traceback (most recent call last):
  # File "py_script2.py", line 5, in <module>
    # my_output = eval(input("輸入表達示: "))
  # File "<string>", line 1, in <module>
# NameError: name '你好' is not defined

# test1
# 輸入表達示3*99
# 297

# practice 2
my_str = input("What's your name?")
print(f"Hi there, {my_str}")

my_int = input("how old are your?")
print(f"{my_int} years old.")
