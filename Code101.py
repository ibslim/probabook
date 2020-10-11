# Random Variable Implementation
# accumulate : Creer un iterateur qui renvoie le resultat accumule en appliquant une operation donnee
from itertools import product, accumulate
from utils import *


#Encapsulate the logic of RV X
# zip : cree un iterateur qui fait l aggregation des elements des collections donnees
# map : applique une fonction sur les elements d'une liste. 


#Test
Omega = set(product({'p','f'},repeat=2)) 
print('Omega         : ',Omega)  
  
map_X = lambda a : a.count('p') 
rv_X  = createFiniteRV(Omega, map_X)     
print('RV dictionary : ',rv_X)

rng_X = set(rv_X.values())               
print('RV Range      : ',rng_X)

inv_X = getInversedFiniteRV(rv_X)        
print('inversed RV   : ', inv_X)
    
prob_Omega = {('f','p'):1/4, ('p','f'):1/4, ('f','f'):1/4, ('p','p'):1/4}   
print('ProbaOmega    : ', prob_Omega)

pdf_X   = probability_X(rv_X, prob_Omega) 
print('P_X RVProbLaw : ',pdf_X)

spdf_X, cdf_X = getCDF(pdf_X)            
print("CDF of X :",cdf_X)
        
#plot pdf and cdf of X
plot_Pdf_Cdf(spdf_X, cdf_X)

#..........................  OUTPUT  ..........................     

# Omega         :  {('f', 'f'), ('p', 'f'), ('p', 'p'), ('f', 'p')}
# RV dictionary :  {('f', 'f'): 0, ('p', 'f'): 1, ('p', 'p'): 2, ('f', 'p'): 1}
# RV Range      :  {0, 1, 2}
# inversed RV   :  {0: {('f', 'f')}, 1: {('p', 'f'), ('f', 'p')}, 2: {('p', 'p')}}
# ProbaOmega    :  {('f', 'p'): 0.25, ('p', 'f'): 0.25, ('f', 'f'): 0.25, ('p', 'p'): 0.25}
# P_X RVProbLaw :  {0: 0.25, 1: 0.5, 2: 0.25}
# CDF of X : {0: 0.25, 1: 0.75, 2: 1.0}