# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:32:25 2020

@author: Me
"""
import pykov
import numpy as np
import networkx as nx
import random

#Classification des etats

dic = { ('s1','s2'): 0.75, ('s1','s3'): 0.25,
          ('s2','s1'):0.5, ('s2','s2'): 0.5,
          ('s3','s4'): 0.4, ('s3','s8'):0.6, 
          ('s4','s3'):0.2,('s4','s5'):0.8,
          ('s5','s6'):1,
          ('s6','s7'):1,
          ('s7','s6'):0.7,('s7','s8'):0.3,
          ('s8','s6'):1}
CM = pykov.Chain(dic)
G=nx.DiGraph(list(CM.keys()))
#la liste des classes de la CM
print(list(nx.strongly_connected_components(G)) )   

# vecteur de proba initial
proba0= pykov.Vector(s1=.3,s2=.4,s3=.1,s4=.1,s5=.1)
proba3=CM.pow(proba0,3)
el2pos={'s1':0,'s2':1,'s3':2,'s4':3,'s5':4,'s6':5,'s7':6,'s8':7}
v1=np.array(proba3._toarray(el2pos).round(2))

print("irreductible? ",nx.is_strongly_connected(G)) # irreducible ou pas
print("periodique? ",nx.is_aperiodic(G)) #periodique ou pas


def ergodic(CM):
    states=CM.states()
    G=nx.DiGraph(list(CM.keys()))
    if((nx.is_strongly_connected(G)) and (nx.is_aperiodic(G))):
        print("La CM est ergodique et les probabilites a l'etat stationnaire sont:")
        print(list(CM.steady()))
        randomState=random.choice(list(states))
        print("Le temps moyen du premier passage des autres etats a l'etat ",randomState," est:",CM.mfpt_to(randomState))
    else:
        succ=CM.succ()
        print("La CM n'est pas ergodique ses classes sont:")
        cfcs=list(nx.strongly_connected_components(G))
        for i in range(len(cfcs)):
            cfc=cfcs[i]
            voisins=set()
            for s in cfc:
                voisins=voisins|set(succ[s].keys())-cfc
            if(len(voisins)>0):
                print("La classe: ",cfc," est transitoire et le temps moyen d'absorption:")
                absorb = CM.absorbing_time(cfc)
                print(absorb)
            else:
                print("La classe: ",cfc," est recurrente")
                randomState=random.choice(list(cfc))
                print("Les probabilites d'absorption par l'etat:",randomState," sont:")
                print(probAbsorb(CM,randomState))
                
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!                
# Ca marche seulement pour les etats absorbants pas pour les classes reccurentes
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def probAbsorb(CM,rs):
    S=CM.states()
    A=np.matrix(np.zeros((len(S),len(S))))
    B=np.matrix(np.zeros((len(S),1)))
    i=0
    for s1 in S:
        if(s1==rs):
            A[i,i]=1
            B[i,0]=1
        else:
            j=0
            for k in S:
                if(k==s1):
                    if(CM.succ(s1)[k]==1):#etat absorbant
                        A[i,j]=1
                    else:
                        A[i,j]=CM.succ(s1)[k]-1
                else:
                    A[i,j]=CM.succ(s1)[k]
                j+=1
        i+=1       
    solution=A.I*B
    return solution
                    
print("FUNCTION CALL1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#ergodic(CM)
print("FUNCTION CALL2>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

dic2 = {   ('s6','s7'):1,
          ('s7','s6'):0.7,('s7','s8'):0.3,
          ('s8','s6'):1}
CM2 = pykov.Chain(dic2)  
ergodic(CM2)      
print("FUNCTION CALL3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
dic3 = {   ('s0','s0'):1,
          ('s1','s0'):0.7,('s1','s2'):0.3,
          ('s2','s1'):0.5,('s2','s3'):0.5,
            ('s3','s3'):1}
CM3= pykov.Chain(dic3)  
#ergodic(CM3)    