#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:47:22 2019

This is a script to convert SAM to BAM files.
"""
#import sys
#command line parameter (SAM file, BED)
#read the file
#input = open('ERR1755082.test.sam', 'r')
#output = open('BED_file', 'w')


import argparse

parser=argparse.ArgumentParser(description = "Convert sam to bed")

parser.add_argument('--samfile', help='sam file input')
parser.add_argument('--bedfile', help='bed file output')
args=parser.parse_args()
input = open(args.samfile, 'r')
output = open(args.bedfile, 'w')



#iterate over each line
for line in input:
    if line.startswith('@'):
        continue
    elif 'XS:A:' not in line:
        continue
  #miss out lines without a strandness
    
    else:
        #split line into strings
        splitline = (line.split('\t'))
        #unmapped reads can't go into the bed file
        if splitline[2] == '*':
            continue
        #unmapped reads can't go into the BED file
        else:  
            chrom = splitline[2]
            SAMfile_start = (int(splitline [3])-1)       #this value is an integer      
            read_length = len(splitline [9])
            gene_name = (splitline[0])
            thestrand = 0
            print(gene_name)
            if 'XS:A:-' in line:
                thestand = '-'
                stop = SAMfile_start        
               #for negative stranded read define the start position of read
                start = stop - read_length
                #the start position for -ve strands will be before the number in column 4
            elif 'XS:A:+' in line:
                thestand = '+'
                start = SAMfile_start    #this value is an integer
                #for +ve strand start position equivalent to column 4 in SAM file
                stop = start + read_length
                #for +ve strand stop position will be after nimber contained in column 4 of strand file
            Bed_line = '%(chrom)s\t(start)s\t%(stop)s\t%(gene_name)s\t.\t%(thestrand)s\n' % locals()
            #see string formatting locals() notes - print line bby line
            #print(Bed_line)
            output.write(Bed_line)

output.close()
#ignore headers
#spilt the line up
#assign each file to a varibale
#create missing variables
#order the variable and print to a new file (BED)
#order: chr, start, stop, read_name, empty, strd.



        
        
