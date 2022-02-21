#Code103.py

from sympy import Symbol
from sympy.stats import Coin	
import sys;sys.path.append('../lib')
from utils import get_Omega,set_Power,set_Filter	        

# class Symbol sets symbols for algebric expressions. "T" for coin tail
# twoTails: checks if the outcome has two tails
twoTails = lambda triple : triple.count(Symbol("T") )==2 	

coin_omega=get_Omega(Coin('Coin'))								
threeCoins_omega = set_Power(coin_omega,3)
has2Tails = set_Filter(twoTails,threeCoins_omega)
print("Event with two tails only : ", has2Tails)

#______________________________   Output  ______________________________________
# Event with two tails only :  {(T, T, H), (H, T, T), (T, H, T)}