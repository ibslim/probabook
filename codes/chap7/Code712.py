# Code712.py

from simpy import Interrupt
from Code709 import e,P,R,TO, rexpo, RSC_Prempt, RQT_prio, RSC_Prio

#
def station(nbClients,serveurs,lamdas,mu,stat, preemption=True):
    times = [ rexpo(l) for l in lamdas ]          # arrival times initialization
    for id in range(nbClients):
        t = min(times)                            # selects the earlier arrival
        priority = times.index(t)                 # gets its priority
        times = [ tc - t for tc in times ]        # updates the arrival times
        times[priority] = rexpo(lamdas[priority]) # generate the next arrival of this priority
        yield TO(t)
        stat[priority][id]=[0,0,0]
        P(client(id,priority,serveurs,mu,stat, e.now, preemption))

#        
def client(id,priority,serveurs,mu,stat, beginTime, preemption=True):
    try:
        stat[priority][id][0] = beginTime
        with RQT_prio(serveurs,priority, preempt=preemption) as req:
            req.time=beginTime
            yield req
            stat[priority][id][1] = e.now
            yield TO(rexpo(mu))
            stat[priority][id][2] = e.now
    except Interrupt:   # in case of preemptive priority
        P(client(id,priority,serveurs,mu,stat, beginTime, preemption))
        
#        
def statistiques(stat):
    rgs = range(len(stat))
    wait_queue, wait_system = [0 for _ in rgs], [0 for _ in rgs]
    for priority in rgs:
        for k in stat[priority].keys():
            wait_queue[priority] += stat[priority][k][1] - stat[priority][k][0]
            wait_system[priority]  += stat[priority][k][2]- stat[priority][k][0]
    print("Wq : Average waiting time in the queue")
    print("W  : Average waiting time in the station")
    
    print("priority \t  Wq \t\t  W ")
    for p in rgs:          
        twq = round(wait_queue[p]/len(stat[p]),2)
        tw = round(wait_system[p]/len(stat[p]),2)
        print(p," \t\t\t ", twq, " \t ", tw)  

#
nbClients, nbServeurs, mu, lamdas, preemption = 100, 1 ,10, [3,4,2], False
stat = [{} for p in range(len(lamdas))]

serveurs = (RSC_Prempt if preemption else RSC_Prio)(nbServeurs)
P(station(nbClients, serveurs, lamdas, mu, stat, preemption)); R()

#
print("Empirical performances:")
statistiques(stat)
