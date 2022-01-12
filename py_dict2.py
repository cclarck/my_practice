#!/usr/bin/env python3
# 01.12.2022 14:49:29 CST
# title = python_dict2

# nested dict
my_elements = {'小美':{'number': 1, 'height':160, 'gender': 'She'},
                '阿明':{'number': 2, 'height':170, 'gender': 'He'}}

my_elements['小美']['weight'] = 0
my_elements['阿明']['weight'] = 80
print(my_elements['小美']['weight'])
print(my_elements['阿明']['weight'])

