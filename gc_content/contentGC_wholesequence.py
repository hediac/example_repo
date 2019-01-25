#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:14:35 2019

@author: hchagrao


calculate GC content in whole sequence

"""

import sys

# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))



input = open(sys.argv[1], "r")


def gc_content(input_sequence):
    count_GC = 0
    count_total = 0

    for x in collect_input:
        if x == 'G' or x == 'C':
            count_GC += 1
        count_total += 1
    
    GC_percent = (count_GC * 100) / count_total
    print("The GC content is equal to {0:.2f} %".format(GC_percent))
    #print("The GC content is equal to ", GC_percent, "%")


#input  = open("Homo_sapiens_CEBPB_sequence.fa","r")
collect_input = ""

sequence_count = 0
name_seq = ""
for line in input:
    if line[0] == ">":
        if sequence_count > 0:
            print(name_seq)
            gc_content(collect_input)
            collect_input = ""
        sequence_count += 1
        name_seq = line.strip()
    else:
        collect_input += line.strip()
print(name_seq)
gc_content(collect_input)


            
        







# testdata = 'CGGGGCTAGGGGCGGGGCTCCGTGGACCAGGGTCCAGCCCCAAGCGGGGCGCGATCCTGC'
