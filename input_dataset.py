import numpy as np 
from io import StringIO
import re

in_path = "Data/keller-train-ca.txt" 		#common_combined_lers.txt,keller-train-ca.txt,austr.txt, test.txt,iris-49-aca.txt
#f = open(in_path,'r')
#test = f.readline()
#print(test)
"""
ts = f.read()
uts = str(ts, "utf-8")
print(uts)
"""
with open(in_path,'r') as f:
	ts = f.read()
	print(ts)
	uts = re.sub(r'\[|\]|\<(.+?)\>','',ts,flags=re.DOTALL)		#\[(.+?)\]

s = StringIO(uts)
try:
	data = np.genfromtxt(s, dtype=None, skip_header=1, comments='!')
	print(type(data))
	print(data)
	print (data[1][1],type(data[1][1]))
except:
	first_reg = re.sub(r'\<(.+?)\>|\!(.+?)','',ts,flags=re.DOTALL)
	sec_reg = re.match(r'(\[(.+?)\])(.+?$)',first_reg,flags=re.DOTALL)
	#print(sec_reg.group(2))
	eles = re.split(r'\n(.+?)\w{?}',sec_reg.group(3))
	#print(eles)
	#for line in 			#count number of attribute and decision 
	#print("Holy shit!")

