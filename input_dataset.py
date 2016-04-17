import numpy as np
import pprint as pp 
from io import StringIO
import re, timeit, collections

def read_dataset(path):
	in_path = "Data/"+path	
	data_sets= []
	first_reg = re.sub(r'\<(.+?)\>|\!(.*?\n)','',open(in_path,'r').read(),flags=re.DOTALL)
	#print(first_reg)
	sec_reg = re.search(r'(\[(.+?)\])(.+?$)',first_reg,flags=re.DOTALL)
	#print(sec_reg)
	attr_d = filter(None, re.split(r'\s+',sec_reg.group(2),flags=re.DOTALL))
	print("attr_d: ", attr_d)
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
	#print(data)
	return data 	

	
	
 
	

	

