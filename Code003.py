from sympy import Symbol
from sympy.stats import Coin, Die, density   	
from itertools import product	
	        
"""
La classe Symbol permet de definir des symbol a manipuler dans des expression algebrique.
Dans cet exemple nous avons definit le symbol "T" qui represente le resultat "pile"
"""
pile=Symbol("T") 
coin = Coin('Coin')									
coin_omega = set(density(coin).dict.keys())	
twoTails = lambda triple : triple.count(pile)==2 
	
threeCoins_omega = set(product(coin_omega,repeat=3))
has2Tails = set(filter(twoTails,threeCoins_omega))
print("Event got two tails only : ", has2Tails)

#..........................  OUTPUT  ..........................     


# Event got two tails only :  {(T, T, H), (H, T, T), (T, H, T)}