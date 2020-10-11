# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:24:48 2020

@author: Me
"""
from scipy.stats import chisquare,chi2
import numpy as np
print(chisquare([8,12,13,14,9,6,8,7,14,9],ddof=0.05))


def autocorr(x, t=1):
    return numpy.corrcoef(numpy.array([x[:-t], x[t:]]))