#Code108.py

import sys;sys.path.append('../lib')
from utils import set_Power,set_Filter, Pe, Pgiven

Omega = set_Power(range(1,7), 2) 

# set_Filter: filters the outcomes having the first element equals 4.
F= set_Filter(lambda a: a[0] == 4,Omega)           
print("F given Event : ", F, ", P(F)=", Pe(Omega,F))

# set_Filter: filters the outcomes having the sum of the 1st and the 2nd elements equals 6.
E= set_Filter(lambda a : a[0] + a[1] == 6,Omega)   
print("E event : ",E, ", P(E)=", Pe(Omega,E))  
   
EF = E & F                                    
print("E and F event : ",EF, ", P(E & F)=", Pe(Omega,EF))     

p_given_F = Pgiven(E,F)                
print("Probability of E given F : ", p_given_F) 

#______________________________   Output  ______________________________________
# F given Event :  {(4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1)} , P(F)= 1/6
# E event :  {(5, 1), (3, 3), (1, 5), (4, 2), (2, 4)} , P(E)= 5/36
# E and F event :  {(4, 2)} , P(E & F)= 1/36
# Probability of E given F :  1/6