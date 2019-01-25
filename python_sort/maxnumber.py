# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a a script to calculate maximum number from a list.

"""

my_list =[26, 54, 93, 17, 77,31, 44, 55, 20, 120]
def find_max(my_list):
    count = 0
    for x in my_list:
        if count == 0:
            maximum = x
        elif x > maximum:
            maximum = x
        count += 1
    print(maximum)     

find_max(my_list)
        
        