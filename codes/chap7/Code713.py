#Code713.py

import simpy
from Code709 import (e,P,R,TO, rexpo, runif, g, RSC_Prempt, SETO, 
                     RQT_prio, gant, randColor)

remain = lambda X,start,speed: X - (e.now - start)*speed # remaining time in the server
# show
def show(evt, s, task, X):
    print(round(e.now,3), " \t " + evt + " \t ",task[0], " \t ", X , 
          " \t ", s.id, " \t ", task[2], " \t ", end='')
    
class Station(object):
        def __init__(self, id, infos): 
            self.id = id; 
            self.Speed = infos['Speed']
            self.Servers = RSC_Prempt(1);
            
        def update(self, task, X, dicTask, evnt, start):
            X = int(remain(X,start,self.Speed))
            dicTask[task[0]]['length'].append((round(start,3),round(e.now-start,3)))
            show(evnt, self, task, X)
            return X
        
        def pf_svc(self, X): delay = X/self.Speed ;   yield TO(delay)
            
        def pf_run(self, task, stations, X, dicTask, preemption=True):
            if X>0:
                try:            
                    with RQT_prio(self.Servers,task[2], preempt=preemption) as s:
                        print([len(s.Servers.queue) for s in stations])
                        yield s;  
                        start = e.now
                        show('S', self, task, X) ; print()
                        yield P(self.pf_svc(X))
                        X = self.update(task, X, dicTask, 'D', start)
                    print([len(s.Servers.queue) for s in stations])
                except simpy.Interrupt:
                    if remain(X,start,self.Speed)>0:
                        X = self.update(task, X, dicTask, 'I', start)
                        P(self.pf_run(task,stations, X, dicTask, preemption))

# create the system: one station for each processor   
def create_system(proc):
        stations = [ Station(i,{'Speed': proc[i]}) for i in range(len(proc))]
        return stations
    
#
def schedule(T,lamda, procs, pmin, pmax, policy, dicTask):
    print('Time \t Event \t Task \t Remain \t Server \t Priority \t Queues')
    stations = create_system(procs)    
    while e.now<T:            
        t = rexpo(lamda) # next arrival
        # creates a new task (Id, length, priority)
        task = yield SETO(e, delay=t, value=('T%d' % next(g), runif(pmin,pmax)*10, runif(1,3)))            
        proc = policy(stations) # calls the specified policy to selects a processor
        # intialize execution structure of the task
        dicTask[task[0]] = {'length':[], 'cpu':proc, 'color':randColor()}
        show('A', stations[proc] , task, task[1])
        # creates the station process associated to the current task
        P(stations[proc].pf_run(task, stations, task[1],  dicTask ))
        
# lessLoaded policy        
def lessLoaded(stations):
    lp = list( map(lambda s: s.Servers.count, stations))
    if(min(lp) == 0): return lp.index(min(lp))
    lq = list( map(lambda s: len(s.Servers.queue), stations))
    return lq.index(min(lq))

# processors speeds, tasks dictionary
processors, dicTask = [3,2,4], {}
# pmin, pmax: minimum and maximum length of tasks, T: simulation time
lamda, pmin, pmax, T = 5, 1, 9, 2
P(schedule(T,lamda,processors, pmin, pmax, lessLoaded, dicTask));  R()

for k,t in dicTask.items():
    print(k," cpu:",t['cpu'],'  length:',t['length'])
lastD = max([d[0]+d[1] for t in dicTask.values() for d in t['length']])    
gant(range(len(processors)),dicTask, int(lastD)+10)

#______________________________   Output  ______________________________________
# T1  cpu: 0   length: [(0.232, 1.872), (25.438, 21.333)]
# T2  cpu: 1   length: [(0.33, 0.647), (50.976, 24.0)]
# T3  cpu: 2   length: [(0.655, 22.5)]
# T4  cpu: 0   length: [(5.438, 20.0)]
# T5  cpu: 1   length: [(0.976, 20.0)]
# T6  cpu: 2   length: [(23.155, 12.5)]
# T7  cpu: 0   length: [(46.771, 6.667)]
# T8  cpu: 1   length: [(20.976, 30.0)]
# T9  cpu: 2   length: [(35.655, 15.0)]
# T10  cpu: 0   length: [(2.104, 3.333)]