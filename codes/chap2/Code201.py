#Code201.py

import sys;sys.path.append('../lib')
from utils import (set_Power, create_FiniteRV, get_InversedFiniteRV,get_PMF,
                    get_CDF,plot_Pdf_Cdf)

# Random Variable Implementation : Encapsulate the logic of RV X. p:Tail, f:head
distribution = {('f','p'):1/4, ('p','f'):1/4, ('f','f'):1/4, ('p','p'):1/4}
   
Omega = set_Power({'p','f'}, 2)           ;print('Omega         : ',Omega)  
prob_Omega = distribution                 ;print('ProbaOmega    : ',prob_Omega)

#map_X: counts the number of tails
map_X = lambda a : a.count('p') 
rv_X  = create_FiniteRV(Omega, map_X)     ;print('RV dictionary : ',rv_X)
rng_X = set(rv_X.values())                ;print('RV Range      : ',rng_X)
inv_X = get_InversedFiniteRV(rv_X)        ;print('inversed RV   : ',inv_X)  
pdf_X   = get_PMF(rv_X, prob_Omega)       ;print('P_X RVProbLaw : ',pdf_X)
pdf_X, cdf_X = get_CDF(pdf_X)             ;print('CDF of X      : ',cdf_X)
        
plot_Pdf_Cdf(pdf_X, cdf_X)

#______________________________   Output  ______________________________________
# Omega         :  {('f', 'p'), ('p', 'p'), ('f', 'f'), ('p', 'f')}
# ProbaOmega    :  {('f', 'p'): 0.25, ('p', 'f'): 0.25, ('f', 'f'): 0.25, ('p', 'p'): 0.25}
# RV dictionary :  {('f', 'p'): 1, ('p', 'p'): 2, ('f', 'f'): 0, ('p', 'f'): 1}
# RV Range      :  {0, 1, 2}
# inversed RV   :  {1: {('p', 'f'), ('f', 'p')}, 2: {('p', 'p')}, 0: {('f', 'f')}}
# P_X RVProbLaw :  {1: 0.5, 2: 0.25, 0: 0.25}
# CDF of X      :  {0: 0.25, 1: 0.75, 2: 1.0}