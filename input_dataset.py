import numpy as np 
from io import StringIO
import re, pprint

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
	col_num = len(A[1,:])
	oc_dict = []
	total_set = []	
	#print(col_num)
	for i in range(0, col_num):	
		V = A[:,i]
		#print("V: ", V)
		unique, counts =  np.unique(V, return_counts=True)
		col_dic = dict(zip(unique, counts))
		oc_dict.append(col_dic)
		col_set = []
		for key, value in col_dic.items():
			#print("key: ",key)
			col_set.append(np.where(V == key))
		total_set.append(col_set)
	pprint.pprint(total_set)
	if len(total_set[:,1]) == 1:
		d = total_set
		A_s = ""
	else:
		d = total_set[-1]
		pre_A = total_set[0:-1]
		
		for sub_set in pre_A[0]:		#
			for elem in sub_set:
			
		
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
 
	

	

