import numpy as np   
import networkx as nx

def makeGraf(S,P):
    dic={}
    succ={s:set() for s in S}
    for i in range(len(S)):
        for j in range(len(S)):
            if(P[i][j]!=0):
                dic[(S[i],S[j])]=P[i][j]  
                succ[S[i]].add(S[j])
    graf=G=nx.DiGraph(list(dic.keys()))
    return graf,succ


def makeAB(S,P):
    n=len(S)
    P1=P.transpose()
    A=np.vstack([P1,[1 for i in range(n)]])
    for i in range(n):
        A[i][i]-=1
    B=np.zeros(n+1)
    B[n]=1
    return A,B
