# Code101.py

from sympy.stats import Coin, Die   
import sys;sys.path.append('../lib')
from utils import get_Omega,set_Product,set_Power	

"""
In this section package sympy.stats is used
class Coin models the coin tossing experiment 
class Die models the die rolling experiment 
"""

Omega1 = {'P','F'}                        ;print("Omega 1 = ",Omega1)
Omega3 = set(range(1,7))                  ;print("Omega 3 = ",Omega3)
Omega5 = set_Product([Omega1,Omega3])     ;print("Omega 5 = ",Omega5)
Omega6 = set_Power(Omega1,3)              ;print("Omega 6 = ",Omega6)

print("\n Using sympy.....................................\n") 	
#R1
coin = Coin('Coin')	
coin_omega=get_Omega(coin)								
print("- R1 Toss a coin omega : ",coin_omega)

#R3
die = Die('Die')
die_omega=get_Omega(die)								
print("- R3 Roll die omega : ",die_omega)

#R6
threeCoins_omega=set_Power(coin_omega,3)
print("- R6 Toss coins omega : ", threeCoins_omega)

#______________________________   Output  ______________________________________
# Omega 1 =  {'P', 'F'}
# Omega 3 =  {1, 2, 3, 4, 5, 6}
# Omega 5 =  {('F', 5), ('P', 1), ('F', 1), ('P', 2), ('F', 2), ('P', 3), 
# ('F', 3), ('F', 6), ('P', 4), ('F', 4), ('P', 5), ('P', 6)}
# Omega 6 =  {('P', 'F', 'P'), ('P', 'P', 'P'), ('F', 'P', 'P'), ('P', 'P', 'F'),
# ('P', 'F', 'F'), ('F', 'P', 'F'), ('F', 'F', 'P'), ('F', 'F', 'F')}

#  Using sympy.....................................

# - R1 Toss a coin omega :  {H, T}
# - R3 Roll die omega :  {1, 2, 3, 4, 5, 6}
# - R6 Toss coins omega :  {(T, T, T), (H, T, T), (H, H, H), (T, H, T), 
#                           (T, T, H), (H, T, H), (T, H, H), (H, H, T)}