import numpy as np
import pprint as pp 
import re, timeit, collections, random

def lem2(g_dict, av_dict):		#g_dict is either lower_dict or upper_dict
	print("In lem2 function...")
	goal_dict = g_dict
	total_fat_T = {}
	#print("g_dict: ", g_dict)
	for key, value in goal_dict.items():
		fat_T = {}
		print("G: ", value)
		G = value
		G_left = G
		while np.size(G)!=0:
			pp.pprint("Instant G: ")
			pp.pprint(G)
			T = []
			T_content = []
			T_G = []	#contain intersection of all [(a,v)] and G and their order 
			g_pos_list = []
			for i in range(0, len(av_dict)):
				T_G.append([i,np.intersect1d(av_dict[i][2], G)])	#only av contains the total information 
			#print("all [a,v] intersected with G: ", T_G)
			while T==[] or set(T_content)!=set(np.intersect1d(T_content, G)):
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
				print("new T_G: ", T_G)
				print("current T: ", T)
				print("T_content: ", T_content)
				print("T_content and G intersection: ", set(T_content)!=set(np.intersect1d(T_content, G)))
			print("T: ", T)
			#print("Length of T: ", len(T))
			#==========smallest while end====================# 
			real_T = []
			if len(T) != 1:
				for p in range(0, len(T)):
					ts_sets = [np.array(T[t][2]) for t in range(0, len(T)) if t!=p]
					print("ts_sets: ", ts_sets)
					#if set(T_content) == set(reduce(np.intersect1d, (ts_sets))):
					real_T_content = set(reduce(np.intersect1d, (ts_sets)))
					print("Fuck: ", ts_sets, real_T_content, value)
					if set(reduce(np.intersect1d, (ts_sets))) < set(value):
						print("less than, True")

						continue
					real_T.append(T[p][0:2])
			else:
				real_T = T[0][0:2]
			print("real_T: ",real_T)		
			if len(fat_T) != 0:
				for T_key, T_value in fat_T.items():
					if set(T_value) == set(np.intersect1d(T_value, T_content)):		#consist element is the subset of new T_content, delete it
						del fat_T[T_key]
			#fat_T[str(real_T)] = #
			#fat_T.append(real_T)
			
			G_left = np.array(list(set(G_left)-set(G)))
			G = G_left
			#print("G_left: ", G_left)
		"""
		if len(fat_T) != 1:
			for f in range(0, len(fat_T)):
		"""
		print("fat_T: ", fat_T)
		#total_fat_T[key] = fat_T
		total_fat_T[key] = fat_T.keys()
	print("total_fat_T: ", total_fat_T)
			
	return total_fat_T
