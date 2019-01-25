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
inf = open(args.samfile, 'r')
output = open(args.bedfile, 'w')



#iterate over each line

count_unmapped = 0


for line in inf:
    if line.startswith('@'):
        continue
    
    else:
        #split line iaccording to tab
        splitline = (line.split('\t'))
        #unmapped reads can't go into the bed file, if unmap star replace chr 
        if splitline[2] == '*':
            count_unmapped =+ 1
            
       
        else:  
            chrom = splitline[2]
            start = (int(splitline[3])-1)       #this value is an integer and account for base 0     
            read_length = len(splitline[9])
            stop = start + read_length
            gene_name = (splitline[0])
            thestrand = "."
            if 'XS:A:-' in line:
                thestand = '-'
            elif 'XS:A:+' in line:
                thestand = '+'
                
                #for +ve strand stop position will be after nimber contained in column 4 of strand file
            bed_line = '%(chrom)s\t%(start)s\t%(stop)s\t%(gene_name)s\t.\t%(thestrand)s\n' % locals()
            #see string formatting locals() notes - print line bby line
            #print(Bed_line)
            output.write(bed_line)
inf.close()
output.close()
#ignore headers
#spilt the line up
#assign each file to a varibale
#create missing variables
#order the variable and print to a new file (BED)
#order: chr, start, stop, read_name, empty, strd.



        
        
