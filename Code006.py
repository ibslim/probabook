from itertools import product
from sympy.stats import Coin,density  	
from sympy import fraction, Symbol
from functools import partial
from fractions import Fraction


Pe = lambda Omega, Event : Fraction(len(Event), len(Omega))
Pde = lambda Omega : { omega : fraction(1,len(Omega)) for omega in Omega}

coin = Coin('Coin')									
coin_Omega = set(density(coin).dict.keys())	
twoCoins_Omega = set(product(coin_Omega , repeat=2))  
print("- Toss 2 Coins Omega : ",twoCoins_Omega)

p_2Coins_Omega = Pde(twoCoins_Omega)                        
print("- Proba map : ",p_2Coins_Omega)   

ev_Property = lambda i, val, omega : omega[i] == val  
ev_Filter =  lambda evProperty , reOmega : set(filter(evProperty, reOmega))

E = ev_Filter(partial(ev_Property,0, Symbol("T")) , twoCoins_Omega) 
p_E = Pe(twoCoins_Omega, E)                                          
print("- Event E : ",E, " Probability : ",p_E)

F = ev_Filter(partial(ev_Property,1, Symbol("T")) , twoCoins_Omega) 
p_F = Pe(twoCoins_Omega, F)                                          
print("- Event F : ",F, " Probabulity : ",p_F)

EF = E & F
p_EF = Pe(twoCoins_Omega, EF)                                        
print("- Event E et F : ",EF, " Probability : ", p_EF)

K = E | F                                                       
p_K = p_E + p_F - p_EF                                                   
print("- Event K (E or F) : ", K, " Probability : ", p_K)

#..........................  OUTPUT  ..........................     

# - Toss 2 Coins Omega :  {(T, T), (H, H), (H, T), (T, H)}
# - Proba map :  {(T, T): (1, 1), (H, H): (1, 1), (H, T): (1, 1), (T, H): (1, 1)}
# - Event E :  {(T, T), (T, H)}  Probability :  1/2
# - Event F :  {(T, T), (H, T)}  Probabulity :  1/2
# - Event E et F :  {(T, T)}  Probability :  1/4
# - Event K (E or F) :  {(T, T), (H, T), (T, H)}  Probability :  3/4