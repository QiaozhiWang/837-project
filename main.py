import numpy as np
import pprint as pp 
from io import StringIO
import re, timeit, collections
from ad_sets import ad_sets, A_set
from cutpoint import entropy
from check_conflict import check_conflict 
from input_dataset import read_dataset

def cutpoint_again():
	return ""

def lem2(vectors):
	
	return ""

def total_cutpoints(vectors):		#use "global equal interval method" 
	cut_start = timeit.default_timer()
	raw_value = vectors[:,:-1].astype(np.float)
	(d_set, a_sets, d_set_dict, a_sets_dict) = ad_sets(vectors[:,-1])	#get d_set, which never change
	d_set = [x.tolist() for x in d_set]
	#print(d_set)
	col_num = len(raw_value[1,:])
	case_num = len(raw_value[:,1])
	#print(col_num)
	#print(case_num)
	new_mat = np.zeros((case_num,col_num+1)).astype(np.str)
	cp_dict = {}
	total_dict = []
	for j in range(0, col_num):		#ignore decision column
		column = raw_value[:,j]
		uniques, counts = np.unique(column, return_counts=True)
		col_dic = dict(zip(uniques, counts))	
		col_dic = sorted(col_dic.items(), key=lambda x: x[0])	#sort by key
		#pp.pprint("**col_dic: ")
		#pp.pprint (col_dic)
		if len(col_dic) == 1:
			new_mat[:,j] = column
			continue
		cp_dict = {}	#cutpoints dictionary
		#==================check whether col_dic only have one element==================#
		v_sum = 0		#used for freq-calculate
		for i in range(0, np.size(uniques)-1):
			mid_point = round((np.float(col_dic[i][0])+np.float(col_dic[i+1][0]))/2,4)
			v_sum += col_dic[i][1]
			cp_dict[mid_point] = round(abs(float(v_sum)/case_num-0.5),4)
		cp_dict = sorted(cp_dict.items(), key=lambda x: x[1]) 	#sort by value
		total_dict.append(cp_dict)
		#----------------if first cutpoint has dulplicated freq-----------------------------#	
		if np.size(cp_dict)/2>1 and cp_dict[1][1] == cp_dict[0][1]:
			fir_cut = min(cp_dict[0][0],cp_dict[1][0])
			#print("**cp_dict[0],cp_dict[1]: ")
			#print(cp_dict[0],cp_dict[1])
		"""
		else:
			if np.size(cp_dict)/2>1:
				print("**cp_dict[0],cp_dict[1]: ")
				print(cp_dict[0],cp_dict[1])
		"""
		#print("**cp_dict[0]: ")
		#print (j, cp_dict[0])
		fir_cut = cp_dict[0][0]
		#print("*Fir_cut: ",fir_cut,"freq: ", cp_dict[0][1])
		#----------------the first time cutpoint calculation for each attribute------------------#
		#----------------Change to symbolic-------------------------------#
		#print(col_dic[0][0], fir_cut)
		pos_1 = np.where((column>=col_dic[0][0])&(column<fir_cut))
		np.put(new_mat[:,j], pos_1, "%s..%s"%(col_dic[0][0],fir_cut))
		pos_2 = np.where(column>fir_cut)
		np.put(new_mat[:,j], pos_2, "%s..%s"%(fir_cut, col_dic[-1][0]))
	new_mat[:,-1] = vectors[:,-1]
	print(new_mat[:,1])
	fir_cut_time = timeit.default_timer()
	print("Time for cutpoints and fir_cut: ", fir_cut_time-cut_start) 
	#--------------check conflicts--------------#
	conflict, cf_set = check_conflict(new_mat,d_set)
	#-------------if conflicts-----------#
	print("!!!!!!!!!Prepare for next cutpoint")
	if conflict:
		next_col = entropy(new_mat,cf_set)
	#pp.pprint(total_dict)		
	return total_dict		#, fir_version
	
def get_interval(attr, times):	#attr: calculate which attribute's cutpoints
	return ""
	 

if __name__ == "__main__":
	"""#------------------for test------------------#
	file_list = ["common_combined_lers.txt","keller-train-ca.txt",
			"austr.txt","iris-49-aca.txt","test.txt"]
	for pf in file_list:
		data = read_dataset(pf)
		print (data)
		#print (data[7][-1])
	#------------------for test------------------#"""
	time1 = timeit.default_timer()	
	#**************read in file name and number K****************#
	#**************upper or lower and output file name****************#
	data = read_dataset("common_combined_lers.txt")
	#print(data[1,:])
	#print(data[:,40])
	time2 = timeit.default_timer()
	print("**Data read time: ", time2-time1)
	values = data[1:]	#contain decision column
	#-----------judge data_type of attributes----------#
	print(values[0][0])
	if not re.match(r'(.+?)(\d+\.\.\d+)(.+?)',values[0][0]):	#If dataset is not symbolied	#15..3.6 \d+\..\d+
		print("***This is not symbolic value dataset. Assume dataset is consistant!")
		cutpoints = total_cutpoints(values)
		 #data[1:][:-1]
	else:
		print("This is symbolic dataset")
		d_set, a_sets, d_set_dict, a_dict_list = ad_sets(values[:,-1])
		cf, cf_set = check_conflict(values[:,0:-1],d_set)
		
		#if cf:
			#readin lower or upper
	#------------------Build_sets----------------------#
	(d_set, a_sets, d_set_dict, a_dict_list) = ad_sets(values)	#There's no conflicts in this kind of data
	time3 = timeit.default_timer()
	#pp.pprint(d_set)
	#pp.pprint(a_sets)
	#pp.pprint(d_set_dict)
	#pp.pprint(a_dict_list)
	#pp.pprint(A_sets)
	print("**Build_sets time: ", time3-time2)
	#print(values[:][:,-1])
	A_set = A_set(values[:,0:-1])
	
	#pp.pprint(d_set)
		
	#pp.pprint(oc_dict)
	#print (data)
	
	#rule_set = lem2(values)
