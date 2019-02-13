#!/usr/bin/env python
import os
import numpy as np
from array import array

mylist = np.array([[1,2,3],[4,5,6],[7,8,9]])
mylist1 = np.delete(mylist, (0), axis=1)
#print(mylist, "This is the end")
#print(mylist1)
list_mean = np.mean(mylist, axis =1)
list_std = np.std(mylist, axis = 1)
print("Calculate Mean")
print(list_mean)
print("And the standard Deviation")
print(list_std)
