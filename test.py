import random

rs = range(0, 12)
remain = rs
while remain:
	print("remain: ", remain)
	select = random.sample(remain, 4)
	remain = set(remain) - set(select)
	print("select: ", select)
	
