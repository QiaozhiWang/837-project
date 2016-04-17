import numpy as np
import pprint as pp 
from io import StringIO
import re, timeit, collections
from ad_sets import ad_sets, A_set
from conflict import lower, upper
from all_cutpoints import total_cutpoints 
from input_dataset import read_dataset

def total_cutpoints(vectors):		#get all [(a,v)] for lem2, change to new matrix
	cut_start = timeit.default_timer()
	raw_value = vectors[:,:-1].astype(np.float)
	(d_set, a_sets, d_set_dict, a_sets_dict) = ad_sets(vectors[:,-1]) #get d_set, which never change
	#print(d_set)
	col_num = len(raw_value[1,:])
	case_num = len(raw_value[:,1])
	#print(col_num)
	#print(case_num)
	sorted_element = []		#all unique elements in the column	
	cp_dict = [] #[[0, '0.8..1.0', array([0, 1, 2])],... format, cutpoints dict, used for lem2
	for j in range(0, col_num):		#ignore decision column
		cp_list = []
		column = raw_value[:,j]
		sorted_element = sorted(np.unique(column))
		start_point = sorted_element[0]
		end_point = sorted_element[-1]
		#print("sorted_element: ",sorted_element)
		if len(sorted_element) == 1:
			cp_dict.append([j,"%s..%s"%(sorted_element[0],sorted_element[0]),range(0, col_num)])
			continue 
		for i in range(0, len(sorted_element)-1):
			mid_point = round((np.float(sorted_element[i])+np.float(sorted_element[i+1]))/2,4)
			cp_list.append(mid_point)	
		for cp in cp_list:
			pos1 = np.where((column>=start_point)&(column<cp))[0]
			cp_dict.append([j,"%s..%s"%(start_point,cp),pos1])
			pos2 = np.where((column>cp)&(column<=end_point))[0]
			cp_dict.append([j,"%s..%s"%(cp, end_point),pos2])
	print("cp_dict: ", cp_dict)
	print("d_set_dict: ", d_set_dict)
	return cp_dict, d_set_dict		#this can be used for lem2	