#Code110.py

from itertools import product

N, p = 4, 0.4

# omega's outcomes are represented as tuples (X,i,j) s.t :
# X is Y if the student knows the answer and N otherwise
# i is the correct answer and j is the given answer 
E = set(product({'N'},set(range(1,N+1)),set(range(1,N+1))))  
F = set([('Y',i,i) for i in range(1,N+1)])  
Omega = F.union(E);  

Dist =  { o : (1-p)/(N*N) if o[0]=='N' else p/N  for o in Omega }
print(Dist)

PF = 0; PEF=0
for i in Omega:
    if i[1] == i[2]: PF  += Dist[i]
    if i[0] == 'Y' : PEF += Dist[i]

print("P(E|F) = %0.5f" % (PEF/PF))
print("Bayes rule: ",N*p/(1+(N-1)*p))

#______________________________   Output  ______________________________________
# {('N', 3, 3): 0.0375, ('Y', 4, 4): 0.1, ('Y', 2, 2): 0.1, ('N', 4, 3): 0.0375,
#  ('N', 3, 2): 0.0375, ('N', 1, 4): 0.0375, ('N', 2, 2): 0.0375, ('N', 4, 4): 0.0375,
#  ('Y', 1, 1): 0.1, ('N', 3, 4): 0.0375, ('N', 1, 3): 0.0375, ('N', 2, 3): 0.0375, 
#  ('N', 1, 2): 0.0375, ('N', 1, 1): 0.0375, ('N', 2, 1): 0.0375, ('Y', 3, 3): 0.1, 
#  ('N', 3, 1): 0.0375, ('N', 2, 4): 0.0375, ('N', 4, 1): 0.0375, ('N', 4, 2): 0.0375}
# P(E|F) = 0.72727
# Bayes rule:  0.7272727272727273
