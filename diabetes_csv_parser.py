#!/usr/bin/env python

import os
import numpy as np
import pandas as pd
import csv
myfilename = "diabetes.tab.txt"

#  This is Class4 Homework

with open(myfilename, 'r') as file_handle:
	diabeteslist = []
	next(file_handle)	#Skips header row 
	for line in file_handle.readlines():
		line_clean = line.replace('   ', ' ').replace('  ', ' ')
		line_clean = line_clean.strip()
		values = line_clean.split('\t')
		caster = []
		for value in values:
			if '.' in value:
				caster.append(float(value))
			else:
				caster.append(int(value))
		diabeteslist += [caster]
print("Display first 2 rows ONLY")
print(diabeteslist[0:2]) #Just printing the first 2 rows
print("End of list!!!. Now Converting Columns to Rows")
rotated_list = [[diabeteslist[jdx][idx]for jdx, row in enumerate(diabeteslist)]for idx, column in 
enumerate(diabeteslist[0])]
print("Diplay first column ONLY")
print(rotated_list[0]) #Just showing the first column rotated to row

print('Homework DONE!!!')









