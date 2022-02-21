# Code708.py

import random
import math
import matplotlib.pyplot as plt
import sys;sys.path.append('../chap5')
from Code502 import getMM1

expo = lambda lmbd : (-1/lmbd)*math.log(random.random())

#
def simul(lamda,mu,maxT):
    clock, n, nb = 0, 0, {}             # n is customers number in the system
    t_arv, t_dep = expo(lamda), maxT    # next arrival/departure/max time      
    arv, dep = [], []                   # Arrival/Departure times
    n_arv, n_dep = 0, 0                 # Arrivals/Departures number 

    #
    def departure():
        nonlocal n_dep, dep, n, t_dep, mu, maxT, clock
        
        n_dep += 1;  dep.append(t_dep)
        if(n >= 0): nb[n] = (nb[n] if n in nb else 0) + t_dep - clock
        n, clock = n-1, t_dep          
        t_dep = clock + expo(mu) if n>0 else maxT 
    
    stats = []
    #
    while(clock < maxT):
        stats.append((clock,n))           # add event id and time 
        if(t_arv < t_dep):                # arrival event            
            
            n_arv += 1; arv.append(t_arv)
            nb[n] = (nb[n] if n in nb else 0) + t_arv - clock 
            n, clock = n+1, t_arv           
            t_arv = clock + expo(lamda)
            
            if(n == 1): t_dep = clock + expo(mu)          
        else:                             # departure event
            departure()
            
    #
    while(n_arv > n_dep):
        stats.append((clock,n))
        departure()        

    prob = {s:nb[s]/clock for s in nb}
    avg_nb_clients = sum(s*prob[s] for s in prob)
    wait = list(map(lambda x, y: x - y, dep, arv))     
    avg_time = sum(wait)/len(wait)
    return(avg_nb_clients,avg_time, stats) 

# 
print('Analytical performances : ');   getMM1(2,3)
print('Empirical performances : ');     nb, tps, stats =simul(2,3,10)
print("Average number of clients in the station: "+str(round(nb,2)))
print("Average response time: " + str(round(tps,2)))  

# Plot
plt.step([t[0] for t in stats], [t[1] for t in stats])
plt.xlabel('Time'); plt.ylabel('clients number')
plt.show()
#______________________________   Output  ______________________________________
# Performances ananlytiques : 
# ==================MM1 =======================
# p0* :0.33333
# p1* :0.22222
# p3* :0.09877
# L   :2.00
# Lq  :1.33
# W   :1.00
# Wq  :0.67
# Performances empiriques : 
# Nombre moyen de clients dans la station:1.97
# Temps de reponse moyen:0.98   
      