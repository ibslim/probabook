#Code105.py

from sympy.stats import Die  	
import sys;sys.path.append('../lib')
from utils import get_Omega, Pe, Pde, set_Filter, set_Power

die_Omega=get_Omega(Die('Die'))								
threeDices_Omega = set_Power(die_Omega , 3)

print("- Drop 3 Dices Omega : ", list(threeDices_Omega)[:4]) 
print("- Omega length : "      , len(threeDices_Omega))

P_3Dices_Omega = Pde(threeDices_Omega) 
print("- Proba mapping : "     , list(P_3Dices_Omega.items())[:4])

# ev_Property: checks if the sum of the two first elements equals the 3rd one 
ev_Property = lambda omega : omega[0] + omega[1] == omega[2]  	
E   = set_Filter(ev_Property, threeDices_Omega) ; print("- E Length: ",len(E))
p_E = Pe(threeDices_Omega, E)                   ; print("- Probability of E : ",p_E)

#______________________________   Output  ______________________________________
# - Drop 3 Dices Omega :  [(4, 2, 2), (1, 4, 4), (2, 2, 4), (5, 5, 1)]
# - Omega length :  216
# - Proba mapping :  [((4, 2, 2), '1/216'), ((1, 4, 4), '1/216'), ((2, 2, 4), '1/216'), ((5, 5, 1), '1/216')]
# - E Length:  15
# - Probability of E :  5/72