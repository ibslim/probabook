#Code102.py

from sympy.stats import Die
import sys;sys.path.append('../lib')
from utils import get_Omega,set_Filter	
 	
print("Events manipulation (operations)")

abc_Omega = {1,2,3,4,5,6}    ;print("Sample space Omega      : ",abc_Omega)
A = {2,5}                    ;print("Event A                 : ", A)
B = {3,4,5}                  ;print("Event B                 : ",B)
isEvent = A < abc_Omega      ;print("is A event of Omega     : ", isEvent)
a_bar = abc_Omega - A        ;print("Complement of A         : ", a_bar)
C = A | B                    ;print("Union of A and B        : ", C)
D = A & B                    ;print("Intersection of A and B : ", D)
E = A - B                    ;print("Difference of A and B   : ", E)
F = A ^ B                    ;print("Symetric Diff A and B   : ", F)

# isEvenNumber: predicate to check if a number is even
isEvenNumber = lambda nb : nb % 2 == 0

die_omega=get_Omega(Die('Die'))	
evenNb =set_Filter(isEvenNumber,die_omega)							
print("Event A even numbers  : ", evenNb) 

evenNbComplement = set(die_omega) - set(evenNb)
print("Event Complement of A : ", evenNbComplement)

#______________________________   Output  ______________________________________
# Events manipulation (operations)
# Sample space Omega      :  {1, 2, 3, 4, 5, 6}
# Event A                 :  {2, 5}
# Event B                 :  {3, 4, 5}
# is A event of Omega     :  True
# Complement of A         :  {1, 3, 4, 6}
# Union of A and B        :  {2, 3, 4, 5}
# Intersection of A and B :  {5}
# Difference of A and B   :  {2}
# Symetric Diff A and B   :  {2, 3, 4}
# Event A even numbers    :  {2, 4, 6}
# Event Complement of A   :  {1, 3, 5}
