#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:52:13 2019
his is a a script to to the bubble sort
@author: hchagrao
"""

my_list =[26, 54, 93, 17, 77,31, 44, 55, 20]

for x in range(0, len(my_list)):
    for y in range(0, len(my_list) -1):
        if my_list[y] > my_list[y+1]:
            temp= my_list[y]
            my_list[y]= my_list[y+1]
            my_list[y+1]= temp
print(my_list)
    