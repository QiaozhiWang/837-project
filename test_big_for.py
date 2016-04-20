import pprint as pp
real_T = [[[[[0,1.0],[1,1.0]]],[0,1]],[[[[0,1.0],[1,1.0]]],[0,1]],[[[[2,1.0],[3,1.0]]],[2,3]]]
value = [0, 1, 2, 3]
total_fat_T = {}

if __name__ == "__main__":
	if len(real_T) != 1:
		Ts_remain = real_T
		for T in real_T:
			#=================delete dulplicated element================#
			Ts_sets = [rT for rT in Ts_remain if rT != T]
			Ts_sets_keys = [Ts[1] for Ts in Ts_sets]
			print("Ts_sets_keys: ", Ts_sets_keys)
			try:
				c_fat_T = set(reduce(np.union1d, (Ts_sets_keys)))
				print("c_fat_T: ", c_fat_T)
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
	total_fat_T["test"] = [f[0] for f in Ts_remain]
	#===========big for loop end================#
	#print("total_fat_T: ")
	pp.pprint (total_fat_T)	