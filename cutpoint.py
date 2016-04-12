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
	#print(col_num)
	cf_num = len(cf_set)
	#print(cf_set)
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
			#print("P: %s/%s"%(value,case_num))
			poss = np.where((column==key))
			val_decisions = [new[:,-1][pos] for pos in poss]
			u, c = np.unique(val_decisions, return_counts=True)
			val_dict = dict(zip(u,c))
			val_sum = 0
			for k, v in val_dict.items():
				p = float(v)/value
				#print("p: %s/%s"%(v,value))
				val_sum += p*(math.log(p,2))
			col_entrp += -(P*val_sum)
		#print("col_entrp: ", col_entrp)
		total_entrp[i] = col_entrp
	#print("total_entrp: ", total_entrp)
	#--------------sort by entropy---------#
	s_entrp = sorted(total_entrp.items(), key=lambda x: x[1])
	print("s_entrp; ", s_entrp)
	#-------if same entropy, select smallest column order--------#
	#---and make sure there possibility to get another cutpoint--#
	find_tag = 0
	for order in range(0, len(s_entrp)):
		if find_tag:
			break 
		#print ("s_entrp[order][1]: ", s_entrp[order][1])
		candi_order_set = [r for r in range(0, len(s_entrp)) if s_entrp[order][1] == s_entrp[r][1]]
		candi_set = [s_entrp[order][0] for order in candi_order_set]
		#print("candi_set: ", candi_set)
		scandi_set = sorted(candi_set)
		for s in range(0, len(scandi_set)):
			candi_col = scandi_set[s]
			print("candi_col: ", candi_col)
			print("lens of total_dict[candi_col]: ", len(total_dict[candi_col]))
			print("col_k_dict[candi_col]-1: ", col_k_dict[candi_col]-1)
			if len(total_dict[candi_col]) == col_k_dict[candi_col]-1:
				continue
			selected_col = candi_col
			col_k_dict[selected_col] = col_k_dict[selected_col]+1 
			new_k = col_k_dict[selected_col]
			find_tag = 1
			break	
	#-----------if all of them have the same entropy 0, select as k and len(total[i])
	if find_tag == 0:		#didn't find selected_col
		for check in range(0,len(col_k_dict)):
			if len(total_dict[check]) == col_k_dict[check]-1:		#all the cutpoints are used
				continue
			selected_col = check
			col_k_dict[selected_col] = col_k_dict[selected_col]+1 
			new_k = col_k_dict[selected_col]
	print("flag:", find_tag, "selected_col: ", selected_col)
	print("col's total dict: ", total_dict[selected_col])
	return selected_col, new_k
	
def cutpoint_again(column, cutpoints_dict, k_int):
	#----------------find the cutpoint-----------------#
	raw_col = column
	#print("raw_col: ", raw_col)
	#col_num = len(raw_col[1,:])
	#case_num = len(raw_col[:,1])
	new_column = np.zeros((1,np.size(raw_col))).astype(np.str)
	cp_list = []
	begin = min(raw_col)
	cp_list.append(begin)
	end = max(raw_col)
	col_cpdict = cutpoints_dict
	#print("col_cpdict: ", col_cpdict)
	for i in range(0, k_int-1):		#k is the length of cutpoint, to index need k-1	
		#print("k_int: ", k_int)	
		#print("i: ", i)
		if i == 0:
			if col_cpdict[i][1] == col_cpdict[i+1][1]:	
				candi = min(col_cpdict[i][0],col_cpdict[i+1][0])
				cp_list.append(candi)
			else: candi = col_cpdict[i][0]
			cp_list.append(candi)
			#print("candi: ", candi)
		if i != 0 and i != k_int-2:
			if col_cpdict[i][1] == col_cpdict[i-1][1]:	#it means the same freq has been selected once
				candi = max(col_cpdict[i][0],col_cpdict[i-1][0])
			elif col_cpdict[i][1] == col_cpdict[i+1][1]:	#it means the same freq selected frist time
					candi = min(col_cpdict[i][0],col_cpdict[i+1][0])
			else: candi = col_cpdict[i][0]
			cp_list.append(candi)
			#print("candi: ", candi)
		if i == k_int-2:
			if col_cpdict[i][1] == col_cpdict[i-1][1]:	
				candi = max(col_cpdict[i][0],col_cpdict[i-1][0])
				cp_list.append(candi)
			else: candi = col_cpdict[i][0]
			cp_list.append(candi)
			#print("candi: ", candi)
	cp_list.append(end)
	#print("cp_list: ")
	#print(cp_list)
	for j in range(0,len(cp_list)-1):
		pos = np.where((raw_col>=cp_list[j]) & (raw_col<=cp_list[j+1])) 
		np.put(new_column, pos, "%s..%s"%(cp_list[j],cp_list[j+1]))
	#print("new_column: ")
	#print(new_column)
	return new_column
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
