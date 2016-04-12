import numpy as np
import pprint as pp 
from io import StringIO
import re, timeit, collections, math
from ad_sets import ad_sets, A_set

def check_conflict(vectors, d):	#vectors-contain decisions
	data_mat = vectors[:,0:-1]
	d_star = d
	non_cf = []
	conflict = False
	BigA = A_set(data_mat)
	#print("BigA:")
	#print(BigA)
	#print("d_set:")
	#print(d_set)
	start = timeit.default_timer()
	fullSet = [i for i in range(0, len(data_mat[:,1]))]
	for sub_A in BigA:
		for sub_d in d_star:
			if set(sub_A) == set(np.intersect1d(sub_A, sub_d)):
				non_cf.extend(sub_A)
				#print(non_cf)
	conflictSet = np.setdiff1d(fullSet,non_cf)
	if len(conflictSet):
		conflict = True
	stop = timeit.default_timer() 
	print("conflict: ", conflict)
	print("conflictSet:")
	print(conflictSet)
	print("**Time of check conflict: ", stop-start)
	return conflict, conflictSet 		#diff is lower set
