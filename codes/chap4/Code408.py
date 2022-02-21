#Code408.py

from CMTC import CMTC

p = [[0.0, 1.0, 0.0],
     [0.0, 0.0, 1.0],
     [1/2, 1/2, 0.0]]
lambdas = [2,1,3]

continuous = CMTC(p, lambdas)
print(continuous.steady_prob())

#______________________________   Output  ______________________________________
#[0.15789474 0.63157895 0.21052632]
