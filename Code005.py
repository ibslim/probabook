from itertools import product		        
from functools import partial
from sympy.stats import Die, density   	
from fractions import Fraction
import random

# Calcule la probabilite d'un evenement dans le cas de l'equiprobabilite
Pe = lambda Omega, Event : Fraction(len(Event), len(Omega))

# Calcule la probabilite d'un evenement elementaire dans le cas de l'equiprobabilite	
Pde = lambda Omega : { omega : str(Fraction(1,len(Omega))) for omega in Omega}


die = Die('Die')
die_Omega = set(density(die).dict.keys()) 
threeDices_Omega = set(product(die_Omega , repeat=3))

print("- Drop 3 Dices Omega : " , list(threeDices_Omega)[:4]) #p3
print("- Omega length : ", len(threeDices_Omega))
P_3Dices_Omega = Pde(threeDices_Omega) 
print("- Proba mapping : ",list(P_3Dices_Omega.items())[:4])

# La fonction qui verifie que la somme des deux premiers egale 
#au resultat du troisieme de	
ev_Property = lambda omega : omega[0]+omega[1] == omega[2]  
ev_Filter =  lambda evProperty , reOmega : set(filter(evProperty, reOmega))
	
E = ev_Filter(ev_Property, threeDices_Omega) ;print("- E Length: ",len(E))
p_E = Pe(threeDices_Omega, E)        
print("- Probability of E : ",p_E)

#..........................  OUTPUT  ..........................     

# - Drop 3 Dices Omega :  [(4, 2, 2), (1, 4, 4), (2, 2, 4), (5, 5, 1)]
# - Omega length :  216
# - Proba mapping :  [((4, 2, 2), '1/216'), ((1, 4, 4), '1/216'), ((2, 2, 4), '1/216'), ((5, 5, 1), '1/216')]
# - E Length:  15
# - Probability of E :  5/72