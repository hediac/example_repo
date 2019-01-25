#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 14:24:26 2019
This is a a script for GC content
@author: hchagrao
"""

testdata= "CGGGGCTAGGGGCGGGGCTCCGTGGACCAGGGTCCAGCCCCAAGCGGGGCGCGATCCTGC"

count_a = 0
count_b = 0
for x in testdata:
    if x == "G":
        count_a += 1
    elif x == "C":
        count_a += 1
    elif x == "A":
        count_b += 1
    elif x == "T":
        count_b += 1
        
print(count_a)
print(count_b)

gc_content_value = count_a/len(testdata)
print(gc_content_value)
print(len(testdata))        

print("GC content: {0:2f} percent".format(gc_content_value))    
    