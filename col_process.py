import numpy as np
import pprint as pp 
from io import StringIO
import re, timeit, collections, random

def col_cutpoints(column,j):		#get all [(a,v)] for lem2, change to new matrix
	print("In total cutpoints...")
	#print("column: ",column)
	column = column.astype(np.float)
	cut_start = timeit.default_timer()
	case_num = len(column)
	#print("case_num: ",case_num)
	sorted_element = []		#all unique elements in the column	
	cp_dict = [] #[[0, '0.8..1.0', array([0, 1, 2])],... format, cutpoints dict, used for lem2
	comp_set = []
	cp_list = []
	sorted_element = sorted(np.unique(column))
	start_point = sorted_element[0]
	end_point = sorted_element[-1]
	#print("sorted_element: ",sorted_element)
	if len(sorted_element) == 1:
		cp_dict.append([j,"%s..%s"%(sorted_element[0],sorted_element[0]),range(0, case_num)])
	else:
		for i in range(0, len(sorted_element)-1):
			mid_point = round((np.float(sorted_element[i])+np.float(sorted_element[i+1]))/2,4)
			cp_list.append(mid_point)	
		for cp in cp_list:
			#print("cp: ", cp)
			pos1 = np.where((column>=start_point)&(column<cp))[0]
			#print("pos1: ", pos1)
			comp_set.append(pos1)
			cp_dict.append([j,"%s..%s"%(start_point,cp),pos1])
			pos2 = np.where((column>cp)&(column<=end_point))[0]
			#print("pos2: ", pos2)
			comp_set.append(pos2)
			cp_dict.append([j,"%s..%s"%(cp, end_point),pos2])
	#print("cp_dict: ")
	#pp.pprint(cp_dict)
	#print("d_set_dict: ")
	#pp.pprint (d_set_dict)
	return cp_dict		#this can be used for lem2	

def col_av(symbolic_col,i):
	print("In av function...")
	col_av_dict = []		#format is the same with cp_dict
	column = symbolic_col
	sorted_element = sorted(np.unique(column))
	for elem in sorted_element:
		pos = np.where((column==elem))[0]
		col_av_dict.append([i, elem, pos])
	#pp.pprint("av_dict: ")
	#pp.pprint(av_dict)
	return col_av_dict


