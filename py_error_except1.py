#!/usr/bin/env python3
# 01.18.2022 17:11:57 CST
# title = error and except

# error 1
# msg = "Hi
# print(msg)

  # File "py_error_except1.py", line 6
    # msg = "Hi
            # ^
# SyntaxError: EOL while scanning string literal

# error 2
# a = int(input('give me a number: '))
# a += 1
# print(a)

# give me a number: one
# Traceback (most recent call last):
  # File "py_error_except1.py", line 15, in <module>
    # a = int(input('give me a number: '))
# ValueError: invalid literal for int() with base 10: 'one'

# error 3
# print(greeting)

# Traceback (most recent call last):
  # File "py_error_except1.py", line 26, in <module>
    # print(greeting)
# NameError: name 'greeting' is not defined

# exception 1
while True:
    try:
        a = int(input("Give me a number: "))
    except ValueError:
        print("It\'s not a vaild number.")
    except KeyboardInterrupt:
        print('\nNo input')
        break
    finally:
        print('\nAttemped Input')
