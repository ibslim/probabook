"""
La fonction partiel(f,X) de functools retourne une fonction en fixant les parametes X 
de la fonction f.

Fraction est une classe qui manipule les nombres rationels
"""

from functools import partial
from fractions import Fraction


# Calcule la probabilite d'un evenement dans le cas de l'equiprobabilite
Pe = lambda Omega, Event : Fraction(len(Event), len(Omega))

# Calcule la probabilite d'un evenement elementaire dans le cas de l'equiprobabilite	
Pde = lambda Omega : { omega : str(Fraction(1,len(Omega))) for omega in Omega}

Omega = {1,2,3,4,5,6}        ;print("Omega               : ", Omega)
A = {2,5}                    ;print("Event A               : ", A)
Pe = partial(Pe,Omega)    
pe_A = Pe(A)                 ;print("Probability of A :"  ,pe_A)
Pde = Pde(Omega)             ;print("Probability App :",Pde)

#..........................  OUTPUT  ..........................     


# Omega               :  {1, 2, 3, 4, 5, 6}
# Event A               :  {2, 5}
# Probability of A : 1/3
# Probability App : {1: '1/6', 2: '1/6', 3: '1/6', 4: '1/6', 5: '1/6', 6: '1/6'}
