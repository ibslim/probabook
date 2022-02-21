#Code104.py

from functools import partial
import sys;sys.path.append('../lib')
from utils import Pe, Pde

# partial: returns a new function from the given one by setting the specified parameters
Omega = {1,2,3,4,5,6}          ;print("Omega               : ", Omega)
A     = {2,5}                  ;print("Event A             : ", A)
Pe    = partial(Pe,Omega)    
pe_A  = Pe(A)                  ;print("Probability of A    : ", pe_A)
Pde   = Pde(Omega)             ;print("Probability App     : ", Pde)

#______________________________   Output  ______________________________________
# Omega              :  {1, 2, 3, 4, 5, 6}
# Event A            :  {2, 5}
# Probability of A   : 1/3
# Probability App    : {1: '1/6', 2: '1/6', 3: '1/6', 4: '1/6', 5: '1/6', 6: '1/6'}
