import numpy as np
import pprint as pp 
from io import StringIO
import re, timeit, collections, math
from ad_sets import ad_sets, A_set

def entropy(mat, cf_set, total_dict, col_k_dict):
	print("**********Entropy function*****************")
	new = np.array([mat[i][:] for i in cf_set])
	col_num = len(new[1,:])-1
	case_num = len(new[:,1])
	print(col_num)
	cf_num = len(cf_set)
	print(new)
	total_entrp = {}
	for i in range(0, col_num):	#
		column = new[:,i]
		uniques, counts = np.unique(column, return_counts=True)
		col_dict = dict(zip(uniques, counts))
		if len(col_dict) == 1:
			continue
		col_entrp = 0
		print(col_dict)
		for key, value in col_dict.items():
			P = float(value)/case_num
			print("P: %s/%s"%(value,case_num))
			poss = np.where((column==key))
			val_decisions = [new[:,-1][pos] for pos in poss]
			u, c = np.unique(val_decisions, return_counts=True)
			val_dict = dict(zip(u,c))
			val_sum = 0
			for k, v in val_dict.items():
				p = float(v)/value
				print("p: %s/%s"%(v,value))
				val_sum += p*(math.log(p,2))
			col_entrp += -(P*val_sum)
		print("col_entrp: ", col_entrp)
		total_entrp[i] = col_entrp
	print("total_entrp: ", total_entrp)
	#--------------sort by entropy---------#
	s_entrp = sorted(total_entrp.items(), key=lambda x: x[1])
	print("s_entrp; ", s_entrp)
	#-------if same entropy, select smallest column order--------#
	#---and make sure there possibility to get another cutpoint--#
	"""
	for order in range(0, col_num):
		candi_set = [r for r in range(0, col_num) if s_entrp[order][1] == s_entrp[i][1])]
		scandi_set = sorted(candi_set)
		for s in range(0, len(scandi_set)):
			
		if not comp:
			break
		candi = min(selected_col, s_entrp[order][0])
		if len(total_dict[candi]) == col_k_dict[candi]-1:
			
	print("selected_col: ", selected_col)
	"""
	
	return selected_col
	
def cutpoint_again(column, cutpoints_dict, k_int):
	#----------------find the cutpoint-----------------#
	
	
	return new_column
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
