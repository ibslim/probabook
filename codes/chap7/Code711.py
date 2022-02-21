#Code711.py

import heapq  # heapqueue allows to allocate servers in round robin policy
from Code709 import e,P,R,TO, rexpo, g, rinverse, RSC_withCapacity, SETO

# ===============================================================================================
# show
def show(cz, args):
    if cz == 2 : print('%7.2f \t %s \t %s \t %s \t %s' % tuple([e.now] + args))
    else       : print('%7.2f \t %s \t %s \t\t %s' % tuple([e.now] + args))

# main method
def carwash(T, topology):  
    class Station(object):
        def __init__(self, id, infos): 
            self.id=id; 
            self.S= infos['S']
            self.M = infos['Mu']
            self.nextStations= infos['nextS']
            self.probas=infos['probas']
            self.Indices = list(range(self.S));  
            self.Servers = RSC_withCapacity(self.S); 
            
        def pf_svc(self, c): X =rexpo(self.M);   yield TO(X)

        # onService 
        def onService(self, id):
            if len(self.Indices) > 0: 
                svr = heapq.heappop(self.Indices);    # pop in queue
                show(2, [id, 'S', svr, self.id])
            return svr

        # onDeparture
        def onDeparture(self,id, svr): 
            heapq.heappush(self.Indices, svr);        # push from queue
            show(1, [id, 'D',self.id])

        # pf_getin : when access a station
        def pf_getin(self, id):   
            show(1, [id, 'A', self.id])                              # Arrival
            with self.Servers.request() as s:
                yield s;                   svr = self.onService(id)  # Service
                yield P(self.pf_svc(id));  self.onDeparture(id, svr) # Departure  
                if self.nextStations != None:
                    i =  rinverse(self.probas)
                    if(i<len(self.nextStations)):
                        P(self.nextStations[i].pf_getin(id)) # go to next station

    # create_system : create the topology
    def create_system(topo):
        stations = [ Station(i,            #  the station's ID
                    { 'S': topo[i][0][0],  # number of servers 
                      'Mu': topo[i][0][1], # service rate
                      'nextS':None ,       # list of next stations      
                      'probas': topo[i][2] # probabilities to go to next stations
                     }) 
                     for i in range(len(topo)) if i!=0]
        # create next stations
        for station in stations:
            if(topo[station.id][1]!=None):
                station.nextStations = [stations[v-1] for v in topo[station.id][1]]
                
        # returns initial stations with their arrival rates       
        return [stations[i-1] for i in topo[0][1]] , topo[0][2] 
    
    # setup the simulation
    def setup():
        def firstS(lamdas):
            t=min(times)
            first=times.index(t)
            for k in range(len(times)): times[k]-=t
            times[first]=rexpo(lamdas[first])
            return first,t
        
        initStations, lamdas = create_system(topo)        

        times=[0 for i in range(len(initStations))]
        for i in range(len(times)): times[i]= rexpo(lamdas[i]) 
        while e.now<T:
            indf, t=firstS(lamdas)
            car = yield SETO(e, delay=t, value='C%d' % next(g))
            P(initStations[indf].pf_getin(car))

    P(setup());  R()

# Test
topo = [
  #(Svr_Nb,mu)  [successors], [Probavility]
  ((None,None), [1,3], [6,2]),
  ((2   ,4   ), [2,3], [0.6,0.2,0.2]),
  ((1   ,3   ), [3]  , [0.5,0.5]),
  ((1   ,6   ), None , None)]

carwash(5,topo)


