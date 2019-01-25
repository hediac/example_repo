#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:22:32 2019


this a script using pysam to convert bam to bed

@author: hchagrao
"""



import argparse
import pysam

parser=argparse.ArgumentParser(description = "Convert bam to bed")

parser.add_argument('--bamfile', help='bam file input')
parser.add_argument('--bedfile', help='bed file output')

args=parser.parse_args()

inf = open(args.bamfile, 'r')
output = open(args.bedfile, 'w')

#open the file as sam from bam "rb"= read binary
# OOP using fetch to go through the object created by pysam.AlignmentFile

samfile= pysam.AlignmentFile(args.bamfile, "rb")
#for read in samfile.fetch():
#    print(read)

count_unmapped = 0
count_none_stop = 0

for read in samfile.fetch():
    if read.is_unmapped == True:
        count_unmapped += 1
    else:
        
#    print(read)    
        chrom = read.reference_name
#    print(chrom)
        start = read.reference_start
#    print(start)
        stop= read.reference_end
#    print(stop)
        name = read.query_name
#    print(name)
        if read.is_reverse == True:
            strand = "-"
        else:
            strand = "+"
        bed_line = '{}\t{}\t{}\t{}\t.\t{}\n'.format(chrom,start,stop,name,strand)    
        output.write(bed_line) 
        
            
print(bed_line)
print(count_unmapped)
print(count_none_stop)   

inf.close()
output.close()    
#   
