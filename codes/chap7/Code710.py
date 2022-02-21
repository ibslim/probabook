# Code710.py

from Code709 import e,P,R,TO, RSC, rexpo, g, show_statistics, ld, onEvent 
import sys;sys.path.append('../chap5')

# =========================================================================
# station entity model
class Station(object):
    def __init__(self, psim):
        self.machines = RSC(e, psim['S']);  
        self.mu = psim['mu']; self.sd = psim['SD']

    def wash(self, voit): 
        yield TO(self.sd(self.mu))

# car entity model
def Car(name, station, psim): 
    # event Arrival, Service, Departure
    onCarEvent = lambda E: onEvent(E, name, psim['staE'])

    # core
    onCarEvent('Arrival')                                    # onArrival event
    with station.machines.request() as machine:
        yield machine;               onCarEvent('Service')   # onService event
        yield P(station.wash(name)); onCarEvent('Departure') # onDeparture event     

# simulation setup 
def setup(psim): 
    station = Station(psim) 
    ld['Nfs']= [psim['S']]
    psim['staE'].append(['I', 0.0, 'None', psim['S'] ,0 ,0 ,0])      # initilize statistics
    while True:
        yield TO(psim['AD'](psim['lambda']))  
        if psim['K']==-1 or len(station.machines.queue) < psim['K']: # Queue Capcity limit
            if(e.now > psim['T_sim']): break                         # Simulation time limit
            P(Car('C%d' % next(g), station, psim))                   # new arrival process

# =============================================================================    

def run_sim(sim, show=False):
    P(setup(sim)); R()                                    # Simulation
    show_statistics(sim, ld, show)                        # Statistic
#
def sim_mmsk(show=False):
    from Code505 import getMMSK
   
    # simulation examples
    sim = {
    'T'     : 'MMSK',      # type of the model
    'mu'    : 4,           # service rate
    'lambda': 10,          # arrival rate
    'S'     : 3,           # number of servers
    'K'     : 30,          # Queue capacity
    'SD'    : rexpo ,      # service distribution
    'AD'    : rexpo,       # arrival distribution
    'T_sim' : 1000,        # Simulation time
    'staE'  : [] }         # Statistics array

    run_sim(sim, show)                                      # simulation
    getMMSK(sim['mu'],sim['lambda'],sim['S'], sim['K'])     # Theory

sim_mmsk()


# def sim_md1(show=False):
#     simulation de la station M/D/1
#     sim = {
#     'T':'MDS',              # type of the model
#     'mu':8,                 # service rate
#     'lambda':6,             # arrival rate
#     'S':1,                  # number of servers
#     'K':-1,                 # Queue capacity
#     'SD': lambda x:1/x ,    # service distribution
#     'AD':rexpo,             # arrival distribution
#     'T_sim':10000,          # Simulation time
#     'staE':[] }             # Statistics array

#     run_sim(sim, show)                                        # simulation
#     print("Performances analytiques :")
#     D , rho = 1/sim['mu'],  sim['lambda']/sim['mu']
#     Wq      = rho/((2/D)*(1-rho));                 
#     W       = D + Wq ;                            
#     Lq      = 1/2*rho**2/(1-rho);                 
#     L       = rho + Lq;                           
#     print("Temps d'attente moyen dans la file      : ", Wq)   
#     print("Temps d'attente moyen dans la station   : ", W) 
#     print("Nombre moyen de clients dans la file    : ", Lq)   
#     print("Nombre moyen de clients dans la station : ", L) 

# sim_md1()
