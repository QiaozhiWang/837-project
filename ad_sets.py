import numpy as np
import pprint as pp 
from io import StringIO
from functools import reduce
import re, timeit, collections

def d_set(ConceptColumn):
	build = timeit.default_timer()
	#print(vectors)
	d_set = []
	d_set_dict = {}		
	uniques =  np.unique(ConceptColumn)
	for key in uniques:
		s_set = np.where(ConceptColumn == key)[0]
		d_set.append(s_set)
		d_set_dict[key] = s_set
	ad_build = timeit.default_timer()
	print("******Time for a and d*********: ", ad_build-build)
	#print("d_set: ", d_set)
	#print("d_set_dict: ", d_set_dict)		
	return d_set, d_set_dict

def numeric_A_set(comp_set,case_num):
	#=====================Use sets' intersection to calculate A===================#
	#----------put all A_sets in one list, except total_set[0]-----------#
	#comp = [sub_set for A_set in total_set[0:-1] for sub_set in A_set] 	
	#print(comp)	
	n_A_set = []		
	comp = comp_set		
	print("comp: ", comp)
	elem_set = np.linspace(0,case_num-1,case_num)		#create set from 0 to casenum-1 for counting
	while True:
		try:		
			print(elem_set[0])
			its_set=[cset for cset in comp if np.in1d(cset,elem_set[0],assume_unique=True).any()]
			print(elem_set[0], its_set)
			
			p_result = reduce(np.intersect1d, (its_set))
			print("p_result: ", p_result)
			n_A_set.append(p_result.tolist())
			print("n_A_set: ", n_A_set)
			elem_set = np.setdiff1d(elem_set,p_result)
			print("elem_set: ", elem_set)
		except:
			break
	
	return n_A_set

def A_set(vectors):	
	#===================Use brute compare to cal A=========================#
	A_build = timeit.default_timer()
	Attrs = vectors.tolist()
	A_set =[]
	#unique_vecs = [vec for vec in set(tuple(x.tolist()) for x in Attrs)]
	vec_set = [list(vec) for vec in set(tuple(x) for x in Attrs)]
	for vec in vec_set:
		#print(vec)
		#A_set.append(np.where(np.prod(vectors==vec,axis=-1))[0])
		A_set.append([pos for pos, y in enumerate(Attrs) if y==vec])
	#print(A_set)
	stop = timeit.default_timer()
	print("****Time for A_set: ", stop-A_build)
	return A_set
