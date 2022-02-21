#Code301.py

import numpy as np    
import random
import sys;sys.path.append('../lib')
from utils import generate_SP,plotSP

fY=lambda : 1 if random.randint(0, 1) else -1   
def generate_BerSum1():
    return generate_SP(fY)

# generate_BerSum2: equavalent version of generate_BerSum1 using umpy.cumsum 
# (cummulative sum of the r.v values)
def generate_BerSum2():
    return np.cumsum([fY() for i in range(1000)])
    
plotSP(generate_BerSum2)


