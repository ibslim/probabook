#Code106.py

from sympy.stats import Coin	
from sympy import Symbol
from functools import partial
import sys;sys.path.append('../lib')
from utils import get_Omega, set_Power, set_Filter, Pde, Pe	
				
coin_Omega=get_Omega(Coin('Coin'))											
twoCoins_Omega = set_Power(coin_Omega, 2)  
print("- Toss 2 Coins Omega : ",twoCoins_Omega)

p_2Coins_Omega = Pde(twoCoins_Omega)                        
print("- Proba map : ",p_2Coins_Omega)   

# ev_Property: checks if the ith element of the outcome equals val
ev_Property = lambda i, val, omega : omega[i] == val  

# set_Filter: filters the given SS using ev_Property with the specified parameters 
E   = set_Filter(partial(ev_Property,0, Symbol("T")) , twoCoins_Omega) 
p_E = Pe(twoCoins_Omega, E)                                          
print("- Event E : ",E, " Probability : ",p_E)

F   = set_Filter(partial(ev_Property,1, Symbol("T")) , twoCoins_Omega) 
p_F = Pe(twoCoins_Omega, F)                                          
print("- Event F : ",F, " Probabulity : ",p_F)

EF   = E & F
p_EF = Pe(twoCoins_Omega, EF)                                        
print("- Event E et F : ",EF, " Probability : ", p_EF)

K   = E | F                                                       
p_K = p_E + p_F - p_EF                                                   
print("- Event K (E or F) : ", K, " Probability : ", p_K)

#______________________________   Output  ______________________________________
# - Toss 2 Coins Omega :  {(H, T), (T, T), (T, H), (H, H)}
# - Proba map :  {(H, T): '1/4', (T, T): '1/4', (T, H): '1/4', (H, H): '1/4'}
# - Event E :  {(T, H), (T, T)}  Probability :  1/2
# - Event F :  {(T, T), (H, T)}  Probabulity :  1/2
# - Event E et F :  {(T, T)}  Probability :  1/4
# - Event K (E or F) :  {(H, T), (T, H), (T, T)}  Probability :  3/4