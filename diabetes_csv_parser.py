#!/usr/bin/env python

import os
import numpy as np
import csv
myfilename = "diabetest.txt"


skip_lines = range(0, 1)	#zero indexed range to skip heading row
with open(myfilename, 'r') as file_handle1,  open("diabetest1.txt", "r+") as file_handle:	#Creates new file to write data without heading
	current_line =0  #Keep a line counter
	for line in file_handle1:	#Read the input file line by line
		if current_line not in skip_lines:
			file_handle.write(line)
		current_line += 1  #To Increase the line counter
#with open("diabetest1.txt", "r") as file_handle:
	diabeteslist = []
	for line in file_handle.readlines():
		line_clean = line.replace('   ', ' ').replace('  ', ' ').replace(',', ' ')
		line_clean = line_clean.strip()
		values = line_clean.split('\t')
#		print(values)
		caster = []
		for value in values:
			try:
				caster +=[int(value)]
			except ValueError as e:
				caster +=[float(value)]
		diabeteslist += [caster]
print(diabeteslist[0:5]) #Just printing the first 5 rows
print("End of list!!!. Now Converting Columns to Rows\n")
rotated_list = [[diabeteslist[jdx][idx] for jdx, row in enumerate(diabeteslist)] for idx, column in 
enumerate(diabeteslist[0])]
print(rotated_list[0]) #Just showing the first column rotated to row
           

print('Finished! \nHomework is DONE')









