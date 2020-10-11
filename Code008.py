from fractions import Fraction
from functools import partial

# Calcule la probabilite d'un evenement dans le cas de l'equiprobabilite
Pe = lambda Omega, Event : Fraction(len(Event), len(Omega))
Pgiven = lambda EventB,EventA :\
    Fraction(len(set(EventA) & set(EventB)), len(EventA))

def itArr(U):
    return [(i,j) for i in U for j in U if i!=j]
	
R = { 'r1' , 'r2', 'r3',  'r4' }
B = { 'b1', 'b2', 'b3', 'b4', 'b5', 'b6' }

Omega=itArr(R | B)
P=partial(Pe,Omega)

A=list(filter(lambda X:X[0][0]=='r',Omega))
print("La probabilite de A:",P(A))

B=list(filter(lambda X:X[1][0]=='r',Omega))
print("La probabilite de B:",P(B))

AB=list(filter(lambda X:X[0][0]=='r' and X[1][0]=='r',Omega))
print("La probabilite de AB:",P(AB))

print("La probabilite de B sachant A:",Pgiven(B,A))

#..........................  OUTPUT  ..........................     

# La probabilite de A: 2/5
# La probabilite de B: 2/5
# La probabilite de AB: 2/15
# La probabilite de B sachant A: 1/3