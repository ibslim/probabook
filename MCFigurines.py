# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 11:04:07 2020

@author: Me
"""
#L;utilisation de array de numpy permet l'utilisation de package "linalg" pour
#les calculs d'algebre lineaire
import numpy as np


#EXEMPLE FIGURINES
S={1,2,3,4}
proba0=np.array([1,0,0,0])
p=np.array([[0.25,0.75,0,0],[0,0.5,0.5,0],[0,0,0.75,0.25],[0,0,0,1]])
proba3=proba0.dot(np.linalg.matrix_power(p,3))
print(proba3)

#Chapman Kolmogorov
n=20
for i in range(n):
    print("Les probabilite de transition apres ",i," etapes sont:")
    print(np.linalg.matrix_power(p,i).round(2))



