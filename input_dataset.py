import numpy as np
import pprint as pp 
from io import StringIO
from functools import reduce
import re

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
	A = vectors
	d_set = []
	A_sets = []
	col_num = len(A[1,:])
	case_num = len(A[:,1])
	print(col_num)
	print(case_num)
	oc_dict = []
	total_set = []	
	for i in range(0, col_num):	
		V = A[:,i]
		#print("V: ", V)
		unique, counts =  np.unique(V, return_counts=True)
		col_dic = dict(zip(unique, counts))
		oc_dict.append(col_dic)			#save for calculate cutpoints
		col_set = []
		for key, value in col_dic.items():
			#print("key: ",key)
			col_set.append(np.where(V == key)[0])
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
		#new_set = elem_set
		for i in elem_set:	#case_num
			print(elem_set)
			its_set=[cset for cset in comp if np.in1d(cset,int(i),assume_unique=True).any()]
			#print(int(i), its_set)
			p_result = reduce(np.intersect1d, (its_set))
			print(p_result)
			elem_set = np.setdiff1d(elem_set,p_result)
			print(elem_set)
			#print(p_result)
			
	return ""	

def lem2(vectors):
	
	return ""

def cutpoints(vectors):		#use "global equal interval method" 
	raw_value = vectors
	for i in range(0, col_num):	
		x, y ,z =  np.unique(data, return_counts=True, return_index=True)
	#col_dic = dict(zip(unique, counts))
	print(x,y,z)
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
	data = read_dataset("test.txt")
	values = data[1:]
	build_sets(values)
	#print (data)
	#-----------judge data_type of attributes----------#
	#if not re.match(r'\d+\.\d+\.\.\d+\.\d+',values[0][0]):
		#data[1:][:-1] = cutpoints(values)
	
	#rule_set = lem2(values)
 
	

	

