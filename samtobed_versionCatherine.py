#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 12:53:16 2019

@author: hchagrao
"""

import sys



#command line parameters for the sam file and bed file
# read in the file

samfile = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'w')
samfile = open('/t1-data/user/hchagrao/Obds/week2/ERR1755082.test.sam' ,'r')
output = open('test.bed','w')

#iterate over the lines
for line in samfile:
   
    if line.startswith('@'):
       
        continue
    elif 'XS:a:' not in line:
       continue
# missout lines wo strandeness
    else:
       #split line into strings
       print(line)
       splitline = (line.split('\t'))
       #unmapped reads can't go into the bed file
       if splitline[2] == '*':
           continue
       # unmapped reads cannot go into bed fie
       else:

           chrom = splitline[2]
           SAMfile_start = (int(splitline[3])-1)
           read_length = len(splitline[9])
           gene_name = splitline[0]
           thestrand =0
           print (gene_name)
           if 'XS:a:-' in line:
               thestrand = '-'
               stop = SAMfile_start
               #for negative strand read define the stop position
               start = stop - read_length
               # the start position for for negative strands will be before the number in column 4
           elif 'XS:a:+' in line:
               thestrand = '+'
               start = SAMfile_start
               #for positive strand position is column 4 in samfile
               stop = start + read_length
               
           Bed_line = '%(chrom)s\t%(start)s\t%(stop)s\t%(gene_name)s\t.\t%(thestrand)s\n' % locals()
           print(Bed_line)
           output.write(Bed_line)
           output.close()
               
               
               