#import itertools
from memory_profiler import profile
from random import randint
import random
from copy import deepcopy
from datetime import datetime

import multiprocessing as mp
import numpy as np

pool = mp.Pool(processes= mp.cpu_count())


def cal_dot(m1, m2, i, j):
	sum = 0
	for k in range(len(m1)):
		sum += m1[k] * m2[k]

	return {"res": sum, "i":i, "j":j}
	

class Matrix:
	def __init__(self, element):
		self.ROW = len(element)
		self.COL = len(element[0])
		self.ELEM = element
	
	def __repr__(self):
		info = "row:{}, col:{}".format(self.ROW, self.COL)
		
		cont = ""
		
		for m in range(self.ROW):
			for n in range(self.COL):
				cont += "{}\t".format(self.ELEM[m][n])
			cont += "\n"
		
		return "{}\n{}".format(info, "")
	
	# def __iter__(self):
	# def __getItem__(self):
	
	def dot(self, B):
		matrix = list()
		if self.COL == B.ROW:
			# 전체 크기는 self.ROW by B.COL
			for i in range(self.ROW):
				col = list()
				for j in range(B.COL):
					sum = 0
					for k in range(self.COL):
						sum += self.ELEM[i][k] * B.ELEM[k][j]
					col.append(sum)
				matrix.append(col)
		else:
			print("ERROR, Matrix info not matched")
		
		return Matrix(matrix)

	def dot_pool(self, B):
		matrix = list()
		results = list()
		if self.COL == B.ROW:
			# 전체 크기는 self.ROW by B.COL
			for i in range(self.ROW):
				col = list()
				# self.ELEM[i] * new list from B`s column
				for j in range(B.COL):
					col.append(B.ELEM[j][i])				
		else:
			print("ERROR, Matrix info not matched")
		
		return Matrix(matrix)
	
@profile
def do_dot(a, b):
	m = Matrix(a)
	n = Matrix(b)
	return m.dot(n)

@profile
def do_dot_pool(a, b):
	m = Matrix(a)
	n = Matrix(b)
	return m.dot_pool(n)

@profile
def make_matrix(row_index, col_index):

	#my_col = [deepcopy(random.uniform(1.1, 1.3))] * col_index
	#mylist = [deepcopy(my_col)] * row_index	
	#mylist = [[random.uniform(1.1, 1.3)] * col_index] * row_index
	mylist = [[randint(1, 10)] * col_index] * row_index
	return mylist
	
	
if __name__ == "__main__":
	
	#r = (idx +1) * 
	#r = (idx +1) * 10
	#r = 80,000,000
	r = 5000000	
	print("count: {:,}".format(r))
	sts = datetime.now()
	a = make_matrix(r, r)
	b = make_matrix(r, r)	
	dot = do_dot(a, b)
	#dot = do_dot_pool(a, b)
	ets = datetime.now()
	print("my time:{}".format((ets - sts)))
	
	sts = datetime.now()
	na = np.array(a)
	nb = np.array(b)		
	na.dot(nb)
	ets = datetime.now()
	print("np time:{}".format((ets - sts)))
	
		
		