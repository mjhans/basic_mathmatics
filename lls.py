from memory_profiler import profile
from random import randint
from datetime import datetime

import multiprocessing as mp
import numpy as np
import json


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
            Xm.append(int(row[1]))
            Xmn.append(Xm)

            Ym1.append([int(row[0])])

    return (Xmn, Ym1,)

if __name__ == "__main__":
    raws = None

    with open("input.json","r") as fp:
        raws = json.load(fp)

    print(raws)
    X, Y = file_open()
    input_data = dict()
    input_data["X"] = X
    input_data["Y"] = Y

    with open("input.json","w") as fp:
        json.dump(input_data, fp)

    np_X = np.array(X, dtype=np.float32)   
    np_XT = np.transpose(np_X)#np_X.T
    np_XT.astype(np.float32)    
    np_Y = np.array(Y, dtype=np.float32)


    print(np_XT.shape, np_X.shape, np_Y.shape)
    XtX_1 = np_XT.dot(np_X)
    #XtX_1.astype(np.int64)
    
    try:        
        I_XtX = np.linalg.inv(XtX_1)
    except numpy.linalg.LinAlgError as err:
    # Not invertible. Skip this one.
        print("{}".format(err))
        pass       
    
    #print("Inverse matrix:{}".format(I_XtX.tolist()))    
    with open("inverse_result_2.csv","w") as fp:
        imat = I_XtX.tolist()
        for mat in imat:
            for m in mat:
                fp.write("{}\n".format(m))

    # get beta hat
    # beta_hat = inverse(Xt X) * Xt*Y
    XtY = np_XT.dot(np_Y)
    beta_hat = I_XtX.dot(XtY)
    #beta_hat = I_XtX.dot(np_XT).dot(np_Y)
    #print("Beta hat:{}".format(beta_hat.tolist()))
    with open("betahat_result_2.csv","w") as fp:
        beta_list = beta_hat.tolist()
        for bhat in beta_list:
            for bh in bhat:
                fp.write("{}\n".format(bh))

    # get Y hat
    # Y_hat = X * beta_hat
    Y_hat = np_X.dot(beta_hat)
    #print("Y_hat:{}".format(Y_hat))

    # 파일쓰기
    with open("Yhat_result1.csv","w") as fp:
        Y_hat_list = Y_hat.tolist()
        for Yhat in Y_hat_list:
            for Yh in Yhat:
                fp.write("{}\n".format(Yh))

    # get ABS(Y_hat - Y)


