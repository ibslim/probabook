import numpy as np


p=0.3
mu=100

Y=np.random.binomial(60,1-p,100000)
X=np.random.poisson(mu*Y)
print("Esperance de Y: ",(Y).mean())
print("Esperance de X: ",(X).mean())

#########################################################
##############           OUTPUT           ###############
# Esperance de Y:  42.0476
# Esperance de X:  4205.3606