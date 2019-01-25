#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 19:56:38 2019

@author: hchagrao
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a a script to calculate maximum number from a list.

"""

my_list =[26, 54, 93, 17, 77,31, 44, 55, 20, 120]
def find_min(my_list):
    count = 0
    for x in my_list:
        if count == 0:
            minimum = x
            min_idx = count
            
     
        elif x < minimum:
            minimum = x
            min_idx = count
        count += 1
    return minimum, min_idx 
find_min(my_list)

for x in range(0, len(my_list)):
     minimum, min_idx = find_min(my_list[x :])  
     my_list[min_idx + x] = my_list[x] 
     my_list[x] = minimum
     print (my_list)