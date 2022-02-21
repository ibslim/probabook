#CMTC.py

import sys
import numpy as np
from CMTD import CMTD

# CMTD subclass of CMTD
class CMTC(CMTD):
    
    # constructor 
    def __init__(self,P, lambdas, S = None, pi0 = None ):
        super().__init__(P ,S ,pi0)
        n = len(P) 
        self.lambdas=np.array(lambdas)
        if((len(self.lambdas) != n)or(len(list(filter(lambda x:x<0,self.lambdas))) != 0)):
            print("lambdas should have ",n," positive values")
            sys.exit(0) 
        copyP = self.P.copy()
        np.fill_diagonal(copyP,-1)
        self.Q = np.matmul(self.lambdas * np.identity(n),copyP)
    
    # steady state probabilities    
    def steady_prob(self):
        n = len(self.S)
        A = np.vstack([self.Q.T,np.ones(n)])
        B = np.append(np.zeros(n),1)  
        return np.linalg.lstsq(A,B)[0]
    
