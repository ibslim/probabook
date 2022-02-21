#Code401.py

import networkx as nx
import numpy as np
import sys;sys.path.append('../lib')
from tools import is_distribution,makeGraf


# CMTD Class 
class CMTD(object):
    
     # constructor 
    def __init__(self,P ,S = None ,pi0 = None):
        n = len(P)
        pi0_default = np.zeros(n); pi0_default[0] = 1
        
        # attributes of CMTD
        self.P = np.array(P)
        self.S = range(1,n+1) if S == None else S
        self.pi0 = pi0_default if pi0 == None else np.array(pi0) 
        
        # checks if P and pi0 are stochastic
        if((len(self.pi0) != n) or (not is_distribution(self.pi0))):
            print("pi0 should be a stochastic vector")
            sys.exit(0)  
        stoc = (len(self.P) == n)
        if(stoc):
            for i in range(n):
                if((len(P[i]) != n) or (not is_distribution(self.P[i]))): 
                    stoc = False;break
        if(not stoc):
            print("P should be a stochastic matrix")
            sys.exit(0)        

