from sympy.stats import DiscreteUniform, density, P ,given
from sympy import symbols
from sympy.logic.boolalg import And, Or, Not  
from fractions import Fraction
from functools import partial
from itertools import product
import time
import math

# Calcule la probabilite d'un evenement dans le cas de l'equiprobabilite
Pe = lambda Omega, Event : Fraction(len(Event), len(Omega))
Pgiven = lambda EventB,EventA : Fraction(len(set(EventA) & set(EventB)), len(EventA))

def itArr(U):
    return [(i,j) for i in U for j in U if i!=j]
	


Omega=set(product(set(range(1,7)),repeat=4))
print(len(Omega))

def twotwo(quad):
    lst, st  =list(quad), set(quad),  #st=set(quad)
    l0=list(st)
    return(len(st)==2 and lst.count(l0[0])==lst.count(l0[1]))

#def deuxdeux(q):
#    return (((q[0]==q[1]) and (q[2]==q[3])and(q[0]!=q[2])) 
#    or ((abs(q[0]-q[1])==abs(q[2]-q[3]))and (q[0]+q[1]==q[2]+q[3])and (q[0]-q[1]!=0)))

A=set(filter(twotwo,Omega))
print(len(A)/len(Omega))

f=math.factorial
Cnk=lambda n,k: f(n)/(f(k)*f(n-k))
prob=lambda F,D,N:Cnk(6,F)*Cnk(D,N)*Cnk(D-N,N)/pow(6,D)
print(prob(2,4,2))
#A=set(filter(deuxdeux,Omega))
#print(len(A))

# P=partial(Pe,Omega)

# A=list(filter(lambda X:X[0][0]=='r',Omega))
# print("La probabilite de A:",P(A))
# B=list(filter(lambda X:X[1][0]=='r',Omega))
# print("La probabilite de B:",P(B))
# AB=list(filter(lambda X:X[0][0]=='r' and X[1][0]=='r',Omega))
# print("La probabilite de AB:",P(AB))

# print("La probabilite de B sachant A:",Pgiven(B,A))
#########################################################
##############           OUTPUT           ###############
