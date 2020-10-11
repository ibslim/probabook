import numpy as np
import random
from statistics import mean
from random import choices

def go_out():
    distance=0
    while True:
        s=choices([1,2,3],prob)[0]
        distance+=10 if s==1 else(7 if s==2 else 5) 
        if(s==1):break
    return distance   

n=100000
prob=[0.5,0.25,0.25]
d=[go_out() for _ in range(n)]

print("Esperance de la distance parcourue=",mean(d))

#########################################################
##############           OUTPUT           ###############
#Esperance de la distance parcourue= 16.00653