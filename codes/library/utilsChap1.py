# utils.py    

import matplotlib.pyplot as plt
from sympy.stats import density
from itertools import accumulate,product
from fractions import Fraction

#---------------------------------------------------------------------------------
# Fraction is a class that respresents rational numbers
Fracstr = lambda p,q : str(Fraction(p,q))

# To format the dictionary values to 2 decimal floats
get_round_dic = lambda dic:{k:round(float(v),2) for k,v in dic.items()} 

# Returns the sample space (SS) of the random experiment (RE)
get_Omega = lambda re: set(density(re).dict.keys()) 

# power: returns cartesian product of a set with itself n times
set_Power = lambda omega,n: set(product(omega,repeat=n))

# product: returns the cartesian product of the given sets
set_Product = lambda omegas: set(product(*omegas))

# filter: selects elements from a set based on some criterion
set_Filter = lambda predicate,collection:set(filter(predicate,collection))

# Pe: returns the probabbility of an event from equally likely SS
Pe  = lambda Omega, Event : Fraction(len(Event), len(Omega))

# Pde: returns the probabbility of an elementary event from equally likely SS
Pde = lambda Omega : { omega : Fracstr(1,len(Omega)) for omega in Omega}

# Pgiven: returns conditional probability of A given B
Pgiven = lambda EventB,EventA :\
    Fraction(len(set(EventA) & set(EventB)), len(EventA))
