# Nous utilisons la fonction prod de numpy qui permet de calculer le produit des elements 
# d'un vecteur

# la bibliotheque plot permet de dessiner le graphique(courbe) de la probabilite
# en fonction du nombre d'enfants n
import numpy as np
import matplotlib.pyplot as plt

n=100
F = lambda n : 1 - np.prod([(365-i)/365 for i in range(n)])
E = [F(i) for i in range(100)]   
print("F(23):",F(23))
print("F(30):",F(30))
print("F(41):", F(41))
print("F(57):", F(57))

#plot
plt.plot(range(n), E, linewidth=1)
xpos = [23, 30, 41, 57]
for xc in xpos: plt.axvline(x=xc, color='r', linewidth=1, linestyle='--')

ypos = [0.5, 0.7, 0.9, 0.99]
for yc in ypos: plt.hlines(y=yc, xmin=0, xmax=100, linewidth=1, color='r', linestyle='--')

plt.xlabel('$n$'); 	plt.ylabel(r'$F(n)$'); plt.title('Birth day problem')    
plt.show()

#..........................  OUTPUT  ..........................     

# F(23): 0.5072972343239857
# F(30): 0.7063162427192688
# F(41): 0.9031516114817354
# F(57): 0.9901224593411699