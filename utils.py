#Code: utils.py

import matplotlib.pyplot as plt
from sympy.stats import FiniteRV, density, cdf
from itertools import accumulate

#retourne un dictionnaire en triant les cles du dictionnaire de la distribution
#donnee en parametre 
def sortPDF(prob_RV):
    return {key:prob_RV[key] for key in sorted(prob_RV.keys())}

#Cree le dictionnaire de la distribution en appliquant la fonction de la v.a decrite par
# map_X aux elements de Omaga
def createFiniteRV(Omega, map_X):
    return dict(zip(Omega, map(map_X, Omega)))
        
# inversed Finite RV X^-1
def getInversedFiniteRV(finiteRV):
    return {v:{i for i in finiteRV.keys() if finiteRV[i] == v } for k,v in finiteRV.items()}
        
#probability law of X P_X
def probability_X(finiteRV, probability_RX):
    inv_X =  getInversedFiniteRV(finiteRV)            
    prob_values = list(map(sum,[[probability_RX[omega] for omega in event] for event in inv_X.values()]))
    return dict(zip(inv_X.keys(), prob_values))
    
#Cumulative distribution function CDF of X
def getCDF(prob_RV):
    sprob_RV = {key:prob_RV[key] for key in sorted(prob_RV.keys())}
    return sprob_RV, dict(zip(sprob_RV.keys(), list(accumulate(sprob_RV.values()))))
    
#plot PDF CDF of RV X
def plot_Pdf_Cdf(pdf, cdf):
    first  = list(cdf.keys())[0]
    last   = list(cdf.keys())[-1]
    keys   = [first-1] + list(cdf.keys()) + [last+1]
    cvalues = [0.0]+ list(cdf.values())
    pvalues = [0.0]+ list(pdf.values())
    
    fig = plt.figure()
    axes = fig.subplots(nrows=1, ncols=2)
    axes[0].bar(keys, pvalues + [0.0], width=0.05)
    axes[1].step(keys, [0.0]+ cvalues)
    plt.show()    

