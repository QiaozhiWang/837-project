import numpy as np
import pprint as pp 
import re, timeit, collections, random

def lem2(g_dict, av_dict):		#g_dict is either lower_dict or upper_dict
	print("In lem2 function...")
	goal_dict = g_dict
	total_fat_T = {}
	#print("g_dict: ", g_dict)
	for key, value in goal_dict.items():
		real_T = []
		#print("G: ", value)
		G = value
		G_left = G
		while np.size(G)!=0:
			#pp.pprint("Instant G: ")
			#pp.pprint(G)
			T = []
			T_content = []
			T_G = []	#contain intersection of all [(a,v)] and G and their order 
			g_pos_list = []
			for i in range(0, len(av_dict)):
				T_G.append([i,np.intersect1d(av_dict[i][2], G)])	#only av contains the total information 
			#print("all [a,v] intersected with G: ", T_G)
			while T==[] or set(T_content)!=set(np.intersect1d(T_content, value)):
				length_set = np.array([len(T_G[i][1]) for i in range(0, len(T_G))])
				#print("length_set: ", length_set)
				max_item = max(length_set)
				#print("max_item: ", max_item)
				g_pos = np.where((length_set==max_item))[0]		#select the av with the largest intersection
				#print("g_pos: ", g_pos)
				if np.size(g_pos) != 1:
					items_num = np.array([len(av_dict[p][2]) for p in g_pos])
					#print("items_num: ", items_num)
					smallest_set = min(items_num)			#if there's a tie, select the smallest set 
					#print("smallest_set: ", smallest_set)
					g_pos = g_pos[np.where((items_num==smallest_set))]				
					if np.size(g_pos)!=1:
						g_pos = min(g_pos)
					#print("g_pos: ", g_pos)
				g_pos_list.append(g_pos)
				if T_content == []:
					T_content = av_dict[g_pos][2]
				T_content = np.intersect1d(av_dict[g_pos][2], T_content)
				T.append(av_dict[g_pos])	#T contains [attribute_number, attribute interval, case_number]
				G = np.intersect1d(T_content, G)	#new_G
				#print("new_G: ", G)
				T_G = []
				for i in range(0, len(av_dict)):
					T_G.append([i,set(np.intersect1d(av_dict[i][2], G))])
				for g in g_pos_list:
					T_G[g][1] = [] 
				#print("new T_G: ", T_G)
				#print("current T: ", T)
				#print("T_content: ", T_content)
				#print("T_content and G intersection: ", set(T_content)!=set(np.intersect1d(T_content, G)))
			#print("T: ", T)
			#print("Length of T: ", len(T))
			#==========smallest while end====================# 
			if len(T) != 1:
				ts_remain = T
				for p in T:
					ts_sets = [t for t in ts_remain if t!=p]
					ts_sets_av = [ts[2] for ts in ts_sets]
					#print("ts_sets_av: ", ts_sets_av)
					try:		#if there's two sets and the redundancy one has been deleted
						c_T_content = set(reduce(np.intersect1d, (ts_sets_av)))
						#print("c_T_content, value: ", c_T_content, value)
						if c_T_content <= set(value):
							#print("Fuck!", c_T_content, value)
							ts_remain = ts_sets
							T_content = list(c_T_content)
					except:
						#print("Two element in set")
						continue
				real_T.append([[tsm[0:2] for tsm in ts_remain],T_content])
			else:
				#print("Shit: ", T[0:1])
				real_T.append([[T[0][0:2]],T_content])
			
			G_left = np.array(list(set(G_left)-set(T_content)))
			G = G_left
			#==========small for loop end=============#
		print("real_T: ",real_T)
		if len(real_T) != 1:
			Ts_remain = real_T
			for T in real_T:
				Ts_sets = [rT for rT in Ts_remain if rT != T]
				Ts_sets_keys = [Ts[1] for Ts in Ts_sets]
				try:
					c_fat_T = set(reduce(np.union1d, (Ts_sets_keys)))
					#print('c_fat_T: ', c_fat_T)
					if c_fat_T == set(value):
						#print("What the fuck!", Ts_sets)
						Ts_remain = Ts_sets
				except:
					continue
			#print("Ts_remain: ", Ts_remain)		
		else:
			Ts_remain = real_T
		#total_fat_T[key] = Ts_remain   		#with av
		total_fat_T[key] = [f[0] for f in Ts_remain]
		#===========big for loop end================#
	print("total_fat_T: ")
	pp.pprint (total_fat_T)	

	return total_fat_T
