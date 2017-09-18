#import itertools
from memory_profiler import profile
from random import randint
from datetime import datetime

import multiprocessing as mp
import numpy as np

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
	
@profile
def do_dot(a, b):
	m = Matrix(a)
	n = Matrix(b)
	return m.dot(n)

@profile
def make_matrix(row_index, col_index):
	row = list()
	for r in range(row_index):
		col = list()
		for c in range(col_index):
			col.append(randint(1, col_index))
		row.append(col)
		
	return row
	
	
if __name__ == "__main__":
	
	for idx in range(1):
		
		r = (idx +1) * 10000000
		a = make_matrix(r, r)
		b = make_matrix(r, r)
		
		sts = datetime.now()
		dot = do_dot(a, b)
		ets = datetime.now()
		print("my time:{}".format((ets - sts)))
		
		na = np.array(a)
		nb = np.array(b)
		sts = datetime.now()
		na.dot(nb)
		ets = datetime.now()
		print("np time:{}".format((ets - sts)))
		
		
		