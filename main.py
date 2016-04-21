import numpy as np
import pprint as pp 
from io import StringIO
import re, timeit, collections, random, math
from ad_sets import d_set, A_set, numeric_A_set
from conflict import lower, upper
from input_dataset import read_dataset
from lem2 import lem2
from col_process import col_cutpoints, col_av

def k_parts(cases_num, k):
	f_num = int(math.ceil(cases_num/float(k)))
	print("Number of cases in each folder: ", f_num)
	rs = range(0, cases_num)
	remain = rs
	k_sets = []
	while remain:
		try:
			#print("remain: ", remain)
			select = random.sample(remain, f_num)
			k_sets.append(select)
			remain = set(remain) - set(select)
			#print("select: ", select)
		except:			#ValueError
			print("Dataset cannot be exactly divided!")
			k_sets.append(list(remain))
			break
	#print("k_sets: ", k_sets)
	return k_sets

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
	cases_num = len(values[:,0]) 
	attr_num = len(values[0,0:-1])
	#print("attr_num: ",attr_num)
	#================divide to k parts============#
	k_sets = k_parts(cases_num, 2)		#Second arg is # of k-folders
	for pf in k_sets:
		#print("pf: ", pf)
		test_mat = [values[pos,:] for pos in pf]
		#test_mat = np.array(test_mat)
		train_mat = np.delete(values, (pf), axis=0)
		#print("train_mat: ", train_mat)
		#print("test_mat: ", test_mat)
		part_A_set = A_set(values[:,0:-1])
		#print("part_A_set: ", part_A_set)
		#A_set = A_set(train_mat[:,0:-1])
		part_d_set, part_d_dict = d_set(train_mat[:,-1])
		#print("d_set_dict: ", d_set_dict)
		#if ul_flag == False			#ul_flag defined as upper=True, lower=False
		lower_set = lower(part_d_dict,part_A_set)  
		#print("Lower: ", lower_set)
		upper_set = upper(part_d_dict,part_A_set)
		#print("Upper: ", upper_set)
		#============Seperate symbolic and numeric dataset==========#
		total_av = []
		for i in range(0, attr_num):	
			col = train_mat[:,i]
			if re.search(r'(\d+\.\.\d+)',col[0]):	
				print("***This is symbolic column!")
				col_av_dict = col_av(col,i)
				total_av.extend(col_av_dict)
				#print("total_av: ", total_av)			
			else:
				print("**This is numeric column")
				cp_dict = col_cutpoints(col,i)
				#print("cp_dict: ", cp_dict)
				total_av.extend(cp_dict)
				#print("total_av: ", total_av)
		total_fat_T = lem2(lower_set, total_av)

	"""
	#-----------judge data_type of every attribute----------#
	
		print("av_dict: "),
		print (av_dict)
		total_fat_T = lem2(lower_set, av_dict)

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
	"""
