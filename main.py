import numpy as np
import pprint as pp 
from io import StringIO
import re, timeit, collections, random
from ad_sets import ad_sets, A_set, numeric_A_set
from conflict import lower, upper
from input_dataset import read_dataset
from lem2 import lem2

def k_parts(vectors, k):
	#???????????if length can't be divided integrately??????????????#
	cases_num = len(vectors[:,1])
	rs = range(0, 12)
	remain = rs
	while remain:
		print("remain: ", remain)
		select = random.sample(remain, 4)
		remain = set(remain) - set(select)
		print("select: ", select)



def total_cutpoints(vectors):		#get all [(a,v)] for lem2, change to new matrix
	print("In total cutpoints...")
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
	comp_set = []
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
			comp_set.append(pos1)
			cp_dict.append([j,"%s..%s"%(start_point,cp),pos1])
			pos2 = np.where((column>cp)&(column<=end_point))[0]
			comp_set.append(pos2)
			cp_dict.append([j,"%s..%s"%(cp, end_point),pos2])
	#print("cp_dict: ")
	#pp.pprint(cp_dict)
	#print("d_set_dict: ")
	#pp.pprint (d_set_dict)
	return cp_dict, d_set_dict, comp_set		#this can be used for lem2	
	
def av(vectors):
	print("In av function...")
	syb_mat = vectors[:,:-1]
	av_dict = []		#format is the same with cp_dict
	for i in range(0, len(syb_mat[1,:])):
		column = syb_mat[:,i]
		sorted_element = sorted(np.unique(column))
		for elem in sorted_element:
			pos = np.where((column==elem))[0]
			av_dict.append([i, elem, pos])
	#pp.pprint("av_dict: ")
	#pp.pprint(av_dict)
	return av_dict

if __name__ == "__main__":
	"""#------------------for test------------------# 
	file_list = ["common_combined_lers.txt","keller-train-ca.txt",
			"austr.txt","iris-49-aca.txt","test.txt"]
	for pf in file_list:
		data = read_dataset(pf)
		print (data)
	#------------------for test------------------#"""
	time1 = timeit.default_timer()	
	data = read_dataset("austr.txt")
	time2 = timeit.default_timer()
	print("**Data read time: ", time2-time1)
	values = data[1:]	#contain decision column
	A_set = A_set(values[:,0:-1])
	#================divide to k parts============#

	#-----------judge data_type of attributes----------#
	if not re.match(r'(.+?)(\d+\.\.\d+)(.+?)',values[0][0]):	
		print("***This is not symbolic value dataset. Assume dataset is consistant!")
		cp_dict, d_set_dict, comp_set = total_cutpoints(values)
		lower_set = lower(d_set_dict, A_set)
		total_fat_T =  lem2(lower_set, cp_dict)
		 #data[1:][:-1]
	else:
		print("This is symbolic dataset")
		d_set, a_sets, d_set_dict, a_dict_list = ad_sets(values[:,-1])
		#if ul_flag == False			#ul_flag defined as upper=True, lower=False
		lower_set = lower(d_set_dict,A_set)  
		print("Lower: ", lower_set)
		upper_set = upper(d_set_dict,A_set)
		print("Upper: ", upper_set)
		av_dict = av(values)
		total_fat_T = lem2(upper_set, av_dict)

	#===========print the result as the formated teacher give==========#
	for concept, situations in total_fat_T.items():
		show_string = ""
		for s in range(0, len(situations)):
			for c in range(0, len(situations[s])-1):
				show_string = show_string+"(%s, %s) & "%(data[0][situations[s][c][0]],situations[s][c][1])
			show_string = show_string+"(%s, %s)"%(data[0][situations[s][-1][0]],situations[s][-1][1])+" -> %s\n"%concept
		print(show_string)
			




	#++++++lower_set same as d_set_dict, av_dict same as cp_dict

		#if cf:
			#readin lower or upper
	#------------------Build_sets----------------------#
	#(d_set, a_sets, d_set_dict, a_dict_list) = ad_sets(values)	#There's no conflicts in this kind of data
	time3 = timeit.default_timer()
	#pp.pprint(d_set)
	#pp.pprint(a_sets)
	#pp.pprint(d_set_dict)
	#pp.pprint(a_dict_list)
	#pp.pprint(A_sets)
	print("**Build_sets time: ", time3-time2) 
	#print(values[:][:,-1])
	#pp.pprint(d_set)
	#pp.pprint(oc_dict)
	#print (data)
	#rule_set = lem2(values)
