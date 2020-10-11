import numpy as np
from functools import reduce
from scipy.stats import bernoulli, binom, poisson, geom, randint, rv_discrete,uniform    
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns

    #
def getbar3Data(Rg_x, Rg_y, p_xy):
    xpos, ypos = reduce(lambda ls, e: ls+[e]*len(Rg_y), Rg_x, []) , [0,1]*len(Rg_x)
    zpos = np.zeros(len(xpos))

    dx, dy = np.ones(len(xpos))*0.02, np.ones(len(xpos))*0.02
    dz = list(p_xy.flatten())
    return xpos, ypos, zpos, dx, dy, dz

    #
def plotjointDistribution(xpos, ypos, zpos, dx, dy, dz):
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')

    ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
    plt.show()
    
    #random variables
Rg_x, Rg_y = np.array([0,1,2]), np.array([0,1])
p_xy = np.array([[1/6,1/4,1/8],[1/8,1/6,1/6]])

    #data for joint distribution plotting
xpos, ypos, zpos, dx, dy, dz = getbar3Data(Rg_x, Rg_y, p_xy)

plotjointDistribution(xpos, ypos, zpos, dx, dy, dz)

    #data for marginal plotting
p_x, p_y = np.sum(p_xy, axis=0), np.sum(p_xy, axis=1)
rv_X = rv_discrete(name='X', values=(Rg_x, p_x)) 
rv_Y = rv_discrete(name='Y', values=(Rg_y, p_y)) 
X, Y = rv_X.ppf(uniform.ppf([0.001, 0.5, 0.999])), rv_Y.ppf(uniform.ppf([0.001, 0.5, 0.999]))    

sns.jointplot(X,Y).set_axis_labels("X", "Y")
    
    