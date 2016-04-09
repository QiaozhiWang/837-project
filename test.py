import os,re

f = open("test.txt",'r')
elements = re.split(r'\s+',f.read(),flags=re.DOTALL)
print(elements)

