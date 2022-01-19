#!/usr/bin/env python3
# 01.19.2022 14:51:18 CST
# title = my_function

def sum_result(num_list):
    return sum(num_list)
    
def mean_result(num_list):
    return sum(num_list) / len(num_list)
    
def add_three(num_list):
    return [n + 3 for n in num_list]
    
def main():
    print("scessful!")

if __name__ == '__main__':
    main()    
