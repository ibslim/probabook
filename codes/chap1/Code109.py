#Code109.py

from functools import partial
import sys;sys.path.append('../lib')
from utils import Pe, Pgiven, set_Filter

# get_diff_pairs: returns cartesian product of U discarding the diagonal elements
def get_diff_pairs(U):
    return [(i,j) for i in U for j in U if i!=j]
	
R = { 'r1' , 'r2', 'r3',  'r4' }
B = { 'b1', 'b2', 'b3', 'b4', 'b5', 'b6' }

Omega=get_diff_pairs(R | B)
P=partial(Pe,Omega)

# selects the outcomes having the 1st element starting with 'r'
A=set_Filter(lambda X:X[0][0]=='r',Omega)
print("Probability of A:",P(A))

B=set_Filter(lambda X:X[1][0]=='r',Omega)
print("Probability of B:",P(B))

AB=set_Filter(lambda X:X[0][0]=='r' and X[1][0]=='r',Omega)
print("Probability of AB:",P(AB))

print("Probability of B given A:",Pgiven(B,A))

#______________________________   Output  ______________________________________
# Probability of A: 2/5
# Probability of B: 2/5
# Probability of AB: 2/15
# Probability of B given A: 1/3