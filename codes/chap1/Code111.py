#Code111.py

from sympy.stats import Coin, density, given, FiniteRV, P
from sympy import Symbol, Eq
import sys;sys.path.append('../lib')
from utils import get_Omega,set_Product

#pmf_i: returns the probability of getting tail in the ith toss of coin omega[0]
pmf_i = (lambda omega, i : 
    (density(cf).dict[omega[i]] if omega[0]==1 else density(cu).dict[omega[i]]))

# The outcome is encoded as follows (H=1, T=2): 
# chosen coin * 100 + 1st toss * 10 + 2nd toss   
encode_omega = (lambda o:
                o[0]*100+(1 if o[1]==H else 2)*10+(1 if o[2] == H else 2))
get_proba = lambda o : PC[o[0]] * pmf_i(o, 1) * pmf_i(o, 2)

H=Symbol('H')

# PC: chosen coin, cu: unfair coin, cf: fair coin 
PC, cu, cf  = { 1:1/2, 2:1/2}, Coin('CU', 1)  , Coin('CF')
omegaPC , omegaC = PC.keys(), get_Omega(cf)

# generates the SS of the experiment (X,Y,Z):
# X is the chosen coin, Y, Z is the outcome of resp, the 1st and 2nd  toss
Omega = set_Product([omegaPC, omegaC, omegaC])
dist = { o: PC[o[0]]* pmf_i(o, 1) * pmf_i(o, 2)  for o in Omega }
print("Distribution : ", dist)

# Encodes the distribution's outcomes as numbers to make it easy for events handling 
dist_encoded = { encode_omega(o) : get_proba(o) for o in Omega } 
print("Encoded distribution : ",dist_encoded)

X    = FiniteRV('X', dist_encoded)
A    = X % 100 < 20   ; print("Probability of getting T in the first toss: %0.2f" % P(A))
B    = X % 10 < 2     ; print("Probability of getting T in the second toss: %0.2f" % P(B))
C    = X < 200        ; print("Probability of choosing the first coin: %0.2f" % P(C))
AB   = Eq(X % 100,11) ; print("Probability of A and B: %0.2f" % P(AB))

AGC  = given(A,C)     ; print("Probability of A|C: %0.2f" % P(AGC))
BGC  = given(B,C)     ; print("Probability of B|C: %0.2f" % P(BGC))
ABGC = given(AB,C)    ; print("Probability of A and B | C: %0.2f" % P(ABGC))

#______________________________   Output  ______________________________________
# Distribution:  {(2, T, T): 0, (2, H, H): 0.5, (2, T, H): 0, (2, H, T): 0,
# (1, T, T): 0.125, (1, H, T): 0.125, (1, T, H): 0.125, (1, H, H): 0.125}
# Encoded distribution:  {222: 0, 211: 0.5, 221: 0, 212: 0, 122: 0.125, 
# 112: 0.125, 121: 0.125, 111: 0.125}
# Probability of getting T in the first toss: 0.75
# Probability of getting T in the second toss: 0.75
# Probability of choosing the first coin: 0.50
# Probability of A and B: 0.62
# Probability of A|C: 0.50
# Probability of B|C: 0.50
# Probability of A and B | C: 0.25