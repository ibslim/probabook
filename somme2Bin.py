import numpy as np
import matplotlib.pyplot as plt
#from collections import Counter

n,m,p,N=10,20,0.2,10000
X=np.random.binomial(n,p,N)
Y=np.random.binomial(m,p,N)
Z=X+Y

print("E(X):",X.mean(),"  E(Y):",Y.mean(),"E(Z):",Z.mean())

Xls=np.linspace(start=1, stop=max(X),num=50 + 1, endpoint=True)
Yls=np.linspace(start=1, stop=max(Y),num=50 + 1, endpoint=True)
Zls=np.linspace(start=1, stop=max(Z),num=50 + 1, endpoint=True)
 
fig = plt.figure()
axes = fig.subplots(nrows=1, ncols=3)
axes[0].hist(X,bins=Xls,density=1,histtype='step',label="Histogramme")
axes[1].hist(Y,bins=Yls,density=1,histtype='step',label="Histogramme")
axes[2].hist(Z,bins=Zls,density=1,histtype='step',label="Histogramme")
plt.show()    

#########################################################
##############           OUTPUT           ###############
#E(X): 1.9769   E(Y): 3.9895 E(Z): 5.9664