import numpy as np
import pprint as pp 
from io import StringIO
import re, timeit, collections, math

def lower(d_dict, A):	#vectors-contain decisions
	d_star_dict = d_dict
	lower_dict = {}
	lower_set = []
	conflict = False
	BigA = A
	#print("A: ", A)
	start = timeit.default_timer()	
	for key,value in d_star_dict.items():
		lower_pd = []		#lower_set for per d_set
		for sub_A in BigA:
			if set(sub_A) == set(np.intersect1d(sub_A, value)):
				#print("sub_A: ", sub_A)
				#print("value: ", value)
				lower_set.extend(sub_A)
				lower_pd.extend(sub_A)
		lower_dict[key] = lower_pd
	#print("lower_dict: ",lower_dict)
	#fullSet = [i for i in range(0, len(data_mat[:,1]))] 
	#print("lower_dict.values: ", lower_dict.values())
	#conflictSet = np.setdiff1d(fullSet,set(lower_set))
	#print("conflict: ", conflictSet)
	#if len(conflictSet):
	#	conflict = True
	stop = timeit.default_timer() 
	print("**Time of check conflict: ", stop-start)
	return lower_dict		#conflict, conflictSet 	#lower = diff conflictSet

def upper(d, A):
	#data_mat = vectors[:,0:-1]
	d_star_dict = d
	upper_dict = {}
	BigA = A
	for key,value in d_star_dict.items():
		upper_pd = []
		for sub_A in BigA:
			if np.in1d(value,sub_A).any()==True:
				upper_pd.extend(sub_A)
		upper_dict[key] = upper_pd
	return upper_dict
	#print("upper_dict: ", upper_dict)




