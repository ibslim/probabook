#Code409.py

from CMTC import CMTC

p = [[0.0, 0.5, 0.5],
     [0.5, 0.0, 0.5],
     [0, 1, 0.0]]
lambdas = [2,2,2]

continuous = CMTC(p, lambdas)
print("Hitting time: ",continuous.hitting_time(3))

#______________________________   Output  ______________________________________
# Hitting time:  [1. 1.]