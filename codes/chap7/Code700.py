#Code700
import numpy as np
import random
import math


def expo(lmbd):
    u=random.random()
    return ((-1/lmbd)*math.log(u))

#
def dox(pevent, psim): #  pnx, pevt, pnb, pn, pclock, ptx, ptd, ptau, pmaxT=0):
    
    pmaxT = psim["dpr"]["max"]
    psim[pevent]["nx"] += 1
    psim[pevent]["ex"].append(psim[pevent]["tx"])
    if(pmaxT == 0 or psim["n"] >= 0): 
        psim["nb"][psim["n"]] = (psim["nb"][psim["n"]] if(psim["n"] in psim["nb"]) else 0) + psim[pevent]["tx"] - psim["clock"]  #else: nb[n]=ta-clock
    psim["n"] += (1 if pevent == "arv" else -1)           
    psim["clock"] = psim[pevent]["tx"]
    psim[pevent]["tx"] = (psim["clock"] + expo(psim[pevent]["taux"])) if(pmaxT == 0 or psim["n"]>0) else pmaxT  #pclock + expo(ptau) 
    
    if(psim["n"] == 1): psim["dpr"]["tx"] = psim["clock"] + expo(psim["dpr"]["taux"])
    
    print(str(psim["clock"]) + " \t " + str(psim["n"]) + " \t " + str(psim[pevent]["nx"]))

#
def simul(tau1,tau2,maxT):
    #
    sim = {
        "n"   : 0, "clock": 0, "nb" : {},          
        "arv" : { "tx" : expo(tau1), "ex": [], "nx" : 0, "taux": tau1 },
        "dpr" : { "tx" : maxT      , "ex": [], "nx" : 0, "taux": tau2  , "max":maxT}, #next arrival time, next departure time      
        }
    
    #
    while(sim["clock"] < maxT):
        dox("arv" if(sim["arv"]["tx"] < sim["dpr"]["tx"]) else "dpr",sim)
        
    #
    while( sim["arv"]["nx"] > sim["dpr"]["nx"]): dox("dpr", sim)  #nd, dep, nb, n, clock, td, td, tau2, maxT)
    
    prob   = {s:sim["nb"][s]/sim["clock"] for s in sim["nb"]}
    avgnb  = sum(s*prob[s] for s in prob)
    wait   = map(lambda x, y: x - y, sim["dpr"]["ex"], sim["arv"]["ex"])    
    l      = list(wait)    
    avgtps = sum(l)/len(l)
    return(round(avgnb,2),round(avgtps,2)) 


nb,tps = simul(2,3,100)
print("Nombre moyen de clients dans la station:"+str(nb)+"  Temps de reponse moyen:"+str(tps))  
#______________________________   Output  ______________________________________
# 0.41408324302814 	 1 	 1
# 0.5497042464653211 	 2 	 2
# 0.6116388198560669 	 1 	 1
# 0.6296262864760898 	 0 	 2
# 0.6654205503868197 	 1 	 3
# 0.6916846815655274 	 2 	 4
# 0.848319495916065 	 3 	 5
#   ...
# Nombre moyen de clients dans la station:1.06  Temps de reponse moyen:0.6  
    
    