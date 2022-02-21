#CMTD.py

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

    # nSteps probabilities
    def nSteps(self,n):
        return self.pi0.dot(np.linalg.matrix_power(self.P,n))
    
    # is_irreducible
    def is_irreducible(self):
        return(nx.is_strongly_connected(makeGraf(self.S,self.P)[0])) 
    
    # is_aperiodic
    def is_aperiodic(self):
        return(nx.is_aperiodic(makeGraf(self.S,self.P)[0])) 

    # is_ergodic
    def is_ergodic(self):
        return (self.is_irreducible() and self.is_aperiodic())

    # classify
    def classify(self):
        graf, succ = makeGraf(self.S,self.P)
        cfcs=list(nx.strongly_connected_components(graf))
        classes={"transitoire":[],"reccurente":[]}
        for i in range(len(cfcs)):
            cfc , voisins = cfcs[i] ,set()
            for s in cfc: voisins = voisins|succ[s]-cfc
            classes["transitoire" if(len(voisins)>0) else "reccurente"].append(cfc) 
        return classes

    # hitting_time : average time to hit for the first time the state given in the argument 
    def hitting_time(self,state):
        n, i = len(self.S), self.S.index(state)
        I = np.identity(n); I[i,i] = 0;   
        g = np.ones(n); g[i]=0;  
        for k in range(n):
            if(self.P[k,k] == 1): I[k,k], g[k] = 0, 0
        return np.matmul(np.linalg.inv(np.identity(n)-np.matmul(I,self.P)), g)
    
    # return_time : average return time to the state given in the argument 
    def return_time(self,state):
        i = self.S.index(state)
        return 1 + ( 0 if self.P[i,i] == 1 else  np.dot(self.P[i], self.hitting_time(state)))

    # absorption probability 
    def absorbing_proba(self,state):
        n, j = len(self.S) , self.S.index(state)
        absorb = [i for i in range(n) if(self.P[i][i] == 1) ]
        if(j not in absorb):
            print("The state must be absorbant")
            sys.exit(0)        
        A, B = np.zeros((n,n)), np.zeros(n)
        A[j][j], B[j] = 1 , 1
        for i in range(n):
            if(i != j):
                if(i in absorb): A[i][i] = 1
                else:
                    for k in range(n):
                        A[i][k] = self.P[i][k] if(k != i) else A[i][i]-1
        return np.linalg.inv(A).dot(B)
   
    # average absorption time
    def absorbing_time(self):
        n = len(self.S)
        absorb = [i  for i in range(n) if(self.P[i][i] == 1)]
        if(len(absorb) == 0):
            print("No absorbant state exists!")
            sys.exit(0)
        A, B = np.zeros((n,n)), np.zeros(n)
        for i in range(n):
            if(i in absorb): A[i][i]=1
            else:
                B[i] = -1
                for j in range(n):
                    if(j not in absorb): A[i][j]=self.P[i][j]
                A[i][i] -= 1
        return np.linalg.inv(A).dot(B)
     
    # steady state probabilities   
    def steady_prob(self):
        if(not self.is_ergodic()):return None
        n = len(self.S)
        A = np.vstack([self.P.T - np.identity(n),np.ones(n)])
        B = np.append(np.zeros(n),1)  
        return np.linalg.lstsq(A,B)[0]
