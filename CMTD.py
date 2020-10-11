import numpy as np
import networkx as nx
import sys
from tools import makeGraf, makeAB


class CMTD(object):   
    def __init__(self,S,P,pi0):
        self.S=S        
        self.P=P
        self.pi0=pi0
        self.graf=None
        self.succ=None
        if(self.is_stoc_mat()==False):
            print("P should be a stochastic matrix")
            sys.exit(0)        
        if(self.is_stoc_vec()==False):
            print("pi0 should be a stochastic vector")
            sys.exit(0)        
   
    def is_stoc_mat(self):
        for i in range(len(self.S)):
            v=[0 if ((self.P[i][j]<=1) and (self.P[i][j]>=0)) else 1 for j in range(len(self.S))]
            if(sum(v)>0): return False
            if(sum(self.P[i])!=1): return False
        return True

    def is_stoc_vec(self):
        n=len(self.pi0)
        if(n!=len(self.S)): return False
        v=[0 if ((self.pi0[j]<=1) and (self.pi0[j]>=0)) else 1 for j in range(n)]
        if(sum(v)>0): return False
        if(sum(pi0)!=1): return False
        return True
    
    def nSteps(self,n):
        return self.pi0.dot(np.linalg.matrix_power(self.P,n))
    
    # def makeGraf(self):
    #     dic={}
    #     succ={s:set() for s in self.S}
    #     for i in range(len(S)):
    #         for j in range(len(S)):
    #             if(self.P[i][j]!=0):
    #                 dic[(self.S[i],self.S[j])]=self.P[i][j]  
    #                 succ[self.S[i]].add(self.S[j])
    #     self.succ=succ
    #     self.graf=G=nx.DiGraph(list(dic.keys()))

    def is_irreducible(self):
        if(self.graf==None):self.graf,self.succ=makeGraf(self.S,self.P)
        return(nx.is_strongly_connected(self.graf)) 
    
    def is_aperiodic(self):
        if(self.graf==None):self.graf,self.succ=makeGraf(self.S,self.P)
        return nx.is_aperiodic(self.graf)
    
    def is_ergodic(self):
        return (self.is_irreducible() and self.is_aperiodic())
    
    def steady_prob(self):
        if(self.is_irreducible()==False):
            print("The MC should be irreducible")
            sys.exit(0) 
        else:
            A,B=makeAB(self.S,self.P)
        steady=np.linalg.lstsq(A,B)
        return steady
    
    # def makeAB(self):
    #     n=len(self.S)
    #     P1=self.P.transpose()
    #     A=np.vstack([P1,[1 for i in range(n)]])
    #     for i in range(n):
    #         A[i][i]-=1
    #     B=np.zeros(n+1)
    #     B[n]=1
    #     return A,B
    
    #Temps moyen du premier passage
    def hitting_time(self,state):
        n=len(self.S)
        j=self.S.index(state)
        absorb=[i  for i in range(n) if(self.P[i][i]==1)]
        A=np.zeros((n,n))
        B=np.zeros(n)
        A[j][j]=1
        for i in range(n):
            if(i!=j):
                if(i not in absorb):
                    B[i]=-1
                    for k in range(n):
                        A[i][k]=self.P[i][k]
                        if(k==i):A[i][k]-=1 
                else:
                    B[i]=np.Inf
                    A[i][i]=1
        solution=np.linalg.inv(A).dot(B)
        return(solution)        
    
    #Temps moyen d'absorption
    def absorbing_time(self):
        n=len(self.S)
        absorb=[i  for i in range(n) if(self.P[i][i]==1)]
        if(len(absorb)==0):
            print("Aucun etat absorbant n'existe")
            sys.exit(0)
        A=np.zeros((n,n))
        B=np.zeros(n)
        for i in range(n):
            if(i in absorb):
                A[i][i]=1
            else:
                B[i]=-1
                for j in range(n):
                    if(j not in absorb):
                        A[i][j]=self.P[i][j]
                A[i][i]-=1
        solution=np.linalg.inv(A).dot(B)
        return(solution)                        
                        

    #Probabilite d'absorption
    def absorbing_proba(self,state):
        n=len(self.S)
        j=self.S.index(state)
        absorb=[i for i in range(n) if(self.P[i][i]==1) ]
        if(j not in absorb):
            print("l'etat doit etre absorbant")
            sys.exit(0)        
        A=np.zeros((n,n))
        B=np.zeros(n)
        A[j][j]=1
        B[j]=1
        for i in range(n):
            if(i!=j):
                if(i in absorb):
                    A[i][i]=1
                else:
                    for k in range(n):
                        if(k!=i):
                            A[i][k]=self.P[i][k]
                        else:A[i][i]-=1
        solution=np.linalg.inv(A).dot(B)
        return(solution)

           
    def classify(self):
        if(self.graf==None):self.makeGraf()
        cfcs=list(nx.strongly_connected_components(self.graf))
        for i in range(len(cfcs)):
            cfc=cfcs[i]
            voisins=set()
            for s in cfc:
                voisins=voisins|self.succ[s]-cfc
            if(len(voisins)>0):
                print("La classe: ",cfc," est transitoire et le temps moyen d'absorption:")
            else:
                print("La classe: ",cfc," est recurrente")
                #randomState=random.choice(list(cfc))


S=["A","B","C","D"]
A=np.array([[1,0,0,0],[1/3,0,2/3,0],[0,1/2,0,1/2],[0,0,0,1]])
pi0=np.array([0,1,0,0])
CM=CMTD(S,A,pi0)
print(CM.absorbing_time())

# S=["A","B","C"]
# A=np.array([[1/2,1/2,0],[0,1/3,2/3],[1/2,1/2,0]])
# pi0=[1,0,0]
# CM=CMTD(S,A,pi0)
# print(CM.steady_prob())

        
    
    

        

