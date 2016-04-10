import numpy as np
import pprint as pp 
from io import StringIO
from functools import reduce
import re, timeit

def read_dataset(path):
	in_path = "Data/"+path		
	with open(in_path,'r') as f:
		ts = unicode(f.read(),'utf-8')
		uts = re.sub(r'\[|\]|\<(.+?)\>','',ts,flags=re.DOTALL)		#\[(.+?)\]
	s = StringIO(uts)
	try:	
		data = np.genfromtxt(s, dtype=None, skip_header=1, comments='!')	
	except:
		print("Holy shit!")
		data_sets= []
		first_reg = re.sub(r'\<(.+?)\>|\!(.+?)','',open(in_path,'r').read(),flags=re.DOTALL)
		sec_reg = re.match(r'(\[(.+?)\])(.+?$)',first_reg,flags=re.DOTALL)
		attr_d = filter(None, re.split(r'\s+',sec_reg.group(2),flags=re.DOTALL))
		data_sets.append(attr_d)	#first row of data_sets is its attris and decision	
		elm_num = len(attr_d)		#elm_num = 16281
		mess_data = filter(None, re.split(r'\s+',sec_reg.group(3),flags=re.DOTALL))
		set_num = len(mess_data)/elm_num		#set_num = 68
		[data_sets.append(mess_data[i*elm_num:(i+1)*elm_num]) for i in range(0, set_num)]
		"""------------check the seperation of mess data in big txt file---------------
		for j in range(0, set_num+1):
			print(data_sets[j][16280]) 
		"""
		data = np.array(data_sets)	#change to ndarry type
	return data 

def build_sets(vectors):
	d_set = []
	A_sets = []
	col_num = len(vectors[1,:])
	case_num = len(vectors[:,1])
	#print(col_num)
	#print(case_num)
	oc_dict = []
	total_set = []	
	for column in vectors.T:	
		#print("V: ", V)
		uniques =  np.unique(column)
		#print(uniques)
		col_set = []
		for key in uniques:
			#print("key: ",key)
			col_set.append(np.where(column == key)[0])
		total_set.append(col_set)
	#pp.pprint(total_set)
	if col_num == 1:
		d_set = total_set
		A_sets = ""
	else:
		d_set = total_set[-1]
		#pp.pprint(d_set)
		#pp.pprint(total_set[0:-1])
		#----------put all A_sets in one list, except total_set[0]-----------#
		comp = [sub_set for A_set in total_set[0:-1] for sub_set in A_set] 	 
		#print(comp)
		elem_set = np.linspace(0,case_num-1,case_num)		
		while True:
			try:		
				#print(elem_set[0])
				its_set=[cset for cset in comp if np.in1d(cset,elem_set[0],assume_unique=True).any()]
				#print(elem_set[0], its_set)
				p_result = reduce(np.intersect1d, (its_set))
				A_sets.append(p_result)
				#print(p_result)
				elem_set = np.setdiff1d(elem_set,p_result)
				#print(elem_set)
				#print(p_result)
			except:
				break
	return d_set, A_sets, oc_dict	

def check_conflict():

	return ""

def lem2(vectors):
	
	return ""

def total_cutpoints(vectors):		#use "global equal interval method" 
	raw_value = vectors
	col_num = len(raw_value[1,:])
	case_num = len(raw_value[:,1])
	#print(col_num)
	#print(case_num)
	cp_dict = {}
	total_dict = []
	for column in raw_value.T:		#ignore decision column
		uniques, counts = np.unique(column, return_counts=True)
		col_dic = dict(zip(uniques, counts))	
		col_dic = sorted(col_dic.items(), key=lambda x: x[0])	#sort by key
		#pp.pprint(col_dic)
		cp_dict = {}	#cutpoints dictionary
		v_sum = 0		#used for freq-calculate
		for i in range(0, np.size(uniques)-1):
			mid_point = round((np.float(col_dic[i][0])+np.float(col_dic[i+1][0]))/2,4)
			v_sum += col_dic[i][1]
			cp_dict[mid_point] = round(abs(float(v_sum)/case_num-0.5),4)
		cp_dict = sorted(cp_dict.items(), key=lambda x: x[1]) 	#sort by value
		total_dict.append(cp_dict)	
		#----------------the first time cutpoint calculation for each attribute------------------#
		print(col_dic[0][0],cp_dict[0][0])
		pos = np.where((column>=col_dic[0][0])&(column<=str(cp_dict[0][0])))[0]
		print(pos)
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
	data = read_dataset("test.txt")
	time2 = timeit.default_timer()
	#print("**Data read time: ", time2-time1)
	values = data[1:]	#contain decision column
	#-----------judge data_type of attributes----------#
	if not re.match(r'\d+\.\d+\.\.\d+\.\d+',values[0][0]):	#If dataset is not symbolied
		print("***This is not symbolic value dataset. Assume dataset is consistant!")
		cutpoints = total_cutpoints(values[:,:-1])
		 #data[1:][:-1]
	else:
		cf = check_conflict()
		#if cf:
			#readin lower or upper
	
	#------------------Build_sets----------------------#
	(d_set, A_sets, oc_dict) = build_sets(values)		#There's no conflicts in this kind of data
	time3 = timeit.default_timer()
	#pp.pprint(A_sets)
	#print("**Build_sets time: ", time3-time2)
	
	#pp.pprint(d_set)
		
	#pp.pprint(oc_dict)
	#print (data)
	
	#rule_set = lem2(values)	
	
 
	

	

