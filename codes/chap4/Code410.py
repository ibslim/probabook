#Code410.py

import numpy as np
from CMTD import CMTD

def getRankPage(G,d):
    N = len(G)
    _output = list( map(lambda x: 0 if list(x).count(1) == 0 else  1/list(x).count(1) , G))
    M = np.identity(N) - d * np.multiply(np.array(_output), G.T).T
    M = np.vstack([M.T ,np.ones(N)])
    B = np.hstack([np.ones(N)*(1-d), N])
    return np.linalg.lstsq(M,B)[0]

# Test with getRankPage
d = 0.85
A = np.array([[0, 1, 1], 
              [1, 0, 0],
              [0, 1, 0]])
print('R : ', getRankPage(A,d))

# Test with the steady state computation
G = [[0.050, 0.475, 0.475],
     [0.900, 0.050, 0.050],
     [0.050, 0.900, 0.050]]
print( 'R : ', CMTD(G).steady_prob()*3)

#______________________________   Output  ______________________________________
# R : [1.16336914 1.19219898 0.64443188]
# R : [1.16336914 1.19219898 0.64443188]

