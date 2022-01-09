#!/usr/bin/env python3
# 01.09.2022 17:20:18 CST
# title = python sring basic operation

first_word = 'Hello'
second_word = 'There'
combine_words = first_word + second_word

# built-in function len()
print(first_word + second_word)
print(len(combine_words))

# notice: \' must be add backslash
long_string = 'Clark\'s skateboard is in the garage.'
print(long_string)

ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
print(ford_quote)

cht_word = '你好'
print(cht_word * 3)
print(len(cht_word))

eng_word = 'Hi'
print(eng_word * 3)
print(len(eng_word))

a_string = "55"
b_string = "66"
number_total = a_string + b_string
print(number_total)

# in python
# >>> len(5566)
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: object of type 'int' has no len()

