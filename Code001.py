# Code001.py
"""
Le code cree l'univers associe a une piece de monnaie en utilsant la structure de donnees
python: ensemble (set,{})   
L fonction product de itertools retourne le produit cartesiens des ensembles donnes en arguments. 
"""
from itertools import product		
"""
Dans cette partie on utilise le package sympy.stats: 
la classe Coin pour modeliser l'experience du lancer d'une piece de monnaie.
la classe Die pour modeliser l'experience du lancer d'un de.
La fonction density qui est definie dans les classes Coin et Die retourne leurs 
univers respectifs.
"""
from sympy.stats import Coin, Die, density          

Omega1 = {'P','F'}                        ;print("Oemag1= ",Omega1)
Omega3 = set(range(1,7))                  ;print("Oemag3= ",Omega3)
Omega5 = set(product(Omega1,Omega3))      ;print("Oemag5= ",Omega5)
Omega6 = set(product(Omega1,repeat=3))    ;print("Oemag6= ",Omega6)

print("\n En utilisant sympy.....................................\n") 	
#R1
coin = Coin('Coin')									
coin_omega = set(density(coin).dict.keys())		    
print("- R1 Toss a coin omega : ",coin_omega)

#R3
die = Die('Die')
die_omega = set(density(die).dict.keys()) 
print("- R3 Roll dice omega : ",die_omega)

#R6
threeCoins_omega = set(product(coin_omega,repeat=3))
print("- R6 Toss coins omega : ", threeCoins_omega)

#______________________________   Output  ______________________________________
# Oemag1=  {'P', 'F'}
# Oemag3=  {1, 2, 3, 4, 5, 6}
# Oemag5=  {('F', 3), ('P', 1), ('F', 1), ('P', 2), ('F', 6), ('P', 3), 
#          ('F', 4), ('F', 5), ('P', 4), ('P', 5), ('P', 6), ('F', 2)}
# Oemag6=  {('P', 'F', 'F'), ('F', 'P', 'F'), ('P', 'P', 'P'), ('F', 'F', 'P'),
#           ('P', 'P', 'F'), ('F', 'P', 'P'), ('F', 'F', 'F'), ('P', 'F', 'P')}

#  En utilisant sympy.....................................

# - R1 Toss a coin omega :  {H, T}
# - R3 Roll dice omega :  {1, 2, 3, 4, 5, 6}
# - R6 Toss coins omega :  {(T, T, T), (H, T, T), (H, H, H), (T, H, T), 
#                           (T, T, H), (H, T, H), (T, H, H), (H, H, T)}