# Code709.py

import random
import simpy
from simpy.resources import resource

# Shared
e =  simpy.Environment()
P = e.process   
R = e.run

# Resources
RSC = simpy.Resource
RSC_withCapacity = lambda cap: simpy.Resource(e, capacity=cap)
RSC_Prempt =  lambda cap: resource.PreemptiveResource( e , capacity = cap )
RSC_Prio =  lambda cap: resource.PriorityResource( e , capacity = cap )
RQT_prio = resource.PriorityRequest

TO = e.timeout
SETO =  simpy.events.Timeout

# load datastructures
ld  = { 'Ls':[],     # Load historique in the system
        'L':[0],     # current load
        'Q':[0],     # current queue
        'tl':[0],    # time when updating the load
        'tq':[0],    # time when updating the queue
        'Nfs':[1]    # Number of servers
        }                        

# updateLoad L/Q
def updateLoad(E, te, h,k, stationId=0):
    global ld
    ld[E][stationId] = ld[E][stationId] + h;     # number of client in Queue Q or System L
    ld['Ls'].append((round(e.now - ld[te][stationId],4), ld[E], k)); ld[te][stationId] =e.now

#
rexpo = lambda mu : random.expovariate(mu)
rinverse = lambda probas : random.choices(range(len(probas)), probas)[0]
runif = lambda a,b : random.randint(a, b)
randColor = lambda:(random.random(),random.random(),random.random())

# iterator for the loop
def geti():
    i=0; 
    while True: i=i+1; yield i
g = geti()

# on Event Arrival +  Sertvice  +  Departure
def onEvent(event, id, stats, stationId=0):
    typEvent = event[0]
    # update system load 
    if typEvent  != 'S': updateLoad('L' ,'tl' ,(1 if typEvent=="A" else -1) ,0, stationId) 
    
    # update system queue
    if ((typEvent  == 'A' and ld['Nfs'][stationId] ==  0) or  
        (typEvent  == 'S' and ld['Q'][stationId] > 0)) : 
        updateLoad('Q' ,'tq' ,(1 if typEvent=="A" else -1) ,1, stationId)  
        
    # update number of available servers
    if typEvent  != 'A': 
        ld['Nfs'][stationId]= ld['Nfs'][stationId] + (1 if typEvent=="D" else -1)

    #statistic array ['E', time, 'ID', servers , L ,Q ,Station]
    stats.append(
        [ typEvent,                       # Event type  Arrival, Service and Departure
          round(e.now,4),                 # time
          id,                             # client id 'ClientID'
          ld['Nfs'][stationId],           # number of available servers
          ld['L'][stationId],             # station load
          ld['Q'][stationId],             # station queue
          stationId                       # station id
          ]                     
        )

# ===========================================================================
# wait_queue   +  wait_system  + 
def process_output(psim):    
    wait_queue, wait_system, N = 0, 0, len(psim)
    for evt in psim:       
        wait_queue   += evt[2] - evt[1]
        wait_system  += evt[3] - evt[1] 
    wait_queue   = round(wait_queue /N,4)
    wait_system  = round(wait_system/N,4)
    return (wait_queue, wait_system)

#
def plot_state(stats0):
    import matplotlib.pyplot as plt
    nbstations =  len(stats0)
    for i in range(nbstations):
        plt.step([v[0] for v in stats0[i].values()], [v[3] for v in stats0[i].values()])
    plt.xlabel('Time');  plt.ylabel('clients number')
    plt.show()

# Statistics
def collect_stats(psim, pld, show, nbstations=1):
    stats0 =[{} for _ in range(nbstations)]
    stats1 =[{} for _ in range(nbstations)]
    eprev, L, Lq = 0, 0, 0
    
    for currentStation in range(len(stats0)):
        stats = stats0[currentStation];  statsW = stats1[currentStation]
        psim0 = [e for e in psim['staE'] if e[6] == currentStation]  # filter stats for the current station
        
        # collect stats [time, [('E', 'ID'),...], Server, Q, L, Station]
        for evt in psim0:
            # stats for the system based on time as key
            if not evt[1] in stats.keys():  # evt[1] time
                stats[evt[1]] = [evt[1], [],0, 0, 0,0]
                stats[evt[1]][2] = evt[3]   # Available servers
                stats[evt[1]][3] = evt[4]   # L
                stats[evt[1]][4] = evt[5]   # Q
            else:
                stats[evt[1]][2] = min(stats[evt[1]][2], evt[3])
                stats[evt[1]][3] = min(stats[evt[1]][3], evt[4])
                stats[evt[1]][4] = min(stats[evt[1]][4], evt[5])
            stats[evt[1]][1].append((evt[0], evt[2])) 
        
            # stats for the system queue : W based on client_ID [ID, A, S, D]
            if evt[2] != 'None':   # evt[2] Client ID
                if not evt[2] in statsW.keys(): statsW[evt[2]] = [evt[2], 0, 0, 0]
                if evt[0]=='A': statsW[evt[2]][1] = evt[1]
                if evt[0]=='S': statsW[evt[2]][2] = evt[1]
                if evt[0]=='D': statsW[evt[2]][3] = evt[1]

            L += (evt[1] - eprev)*evt[4]
            Lq += (evt[1] - eprev)*evt[5]
            eprev = evt[1]
            
        wqs = process_output(statsW.values())
        lds = (round(L/psim['T_sim'],4), round(Lq/psim['T_sim'],4))
        return wqs, lds, stats0 
        
# show_statistics
def show_statistics(psim, pld, show, nbstations=1):
    wqs, lds, sta = collect_stats(psim, pld, show, nbstations)#
    if show :
        for e in sta:
            for v in e.values() : print(v)

    print("Empirical performances :")
    print("Average time in the queue               : ", wqs[0])   
    print("Average time in the system              : ", wqs[1]) 
    print("Average number of clients in the queue  : ", lds[1])  
    print("Average number of clients in the system : ", lds[0])  
    plot_state(sta)

# =========================================================================== 
# method that plots the gant chart of the application
def gant(cpus, tasks,l, H=50, M=5 ):
    import matplotlib.pyplot as plt  
    fig, axi = plt.subplots()  
    axi.set_ylim(0, H);      axi.set_xlim(0, l)        
    axi.set_xlabel('Time');  axi.set_ylabel('Processor')        
    axi.grid(True)
    
    # Setting ticks on y-axis
    dx =  int((H - 2*M)/ len(cpus))
    axi.set_yticks([dx + i*dx  for i in range(len(cpus))])           
    axi.set_yticklabels(cpus)
    
    # Declaring a bar in schedule
    for k,task in tasks.items():
        posH=(task['cpu']+1)*dx-M/2
        axi.broken_barh(task['length'], (posH, M) , facecolors = task['color'])       
        for t in task['length']:
            axi.annotate(k, (1,1), xytext=(t[0]+t[1]/2-1, posH+M+1))
    plt.show() 