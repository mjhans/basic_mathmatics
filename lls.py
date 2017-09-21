from memory_profiler import profile
from random import randint
from datetime import datetime

import multiprocessing as mp
import numpy as np


from matrix import Matrix
import csv

def file_open():
    Xmn = list()
    Ym1 = list()
    with open("app_data.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')        
        for row in readCSV:
            Xm = list()
            Xm.append(1)
            Xm.append(float(row[1]))
            Xmn.append(Xm)

            Ym1.append([float(row[2])])

    return (Xmn, Ym1,)

if __name__ == "__main__":
    X, Y = file_open()
    np_X = np.array(X)
    np_XT = np_X.T
    np_Y = np.array(Y)

    print(np_X.shape, np_Y.shape, np_X.T.shape)
    XtX = np_X.T.dot(np_X)
    print(XtX)


    mat_X = Matrix(X)
    mat_Y = Matrix(Y)

    print("{}, {}, {}".format(mat_X, mat_Y, mat_X.T()))
    XtX = mat_X.T().dot(mat_X)
    print(XtX.ELEM)
