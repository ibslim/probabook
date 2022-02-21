#Code501.py

from math import factorial

# Queueing Class 
class Queueing(object):
    
    # constructor 
    def __init__(self, model='MM1',  A='M' ,B='M' ,C=1, K=-1, P=None, D='FIFO', laws =None):
        self.model =  model
        
        self.s, self.k = C, K
        self.lamda, self.mu = A['params']['lambda'], B['params']['mu']
        self.rho = 1.0 * self.lamda/(self.s*self.mu)
                
        self.p0 = laws[self.model]['p0'](rho1=self.rho, s=self.s , k=self.k)
        self.pk = self.pn(self.k) if self.k > 0 else 0;  
        self.lamdae = (1 - ( 0 if self.k == -1 else self.pk)) * self.lamda
        self.rhoe = 1.0 * self.lamdae/(self.s* self.mu)

        #        
        self.Lq = laws[self.model]['Lq'](rho1=self.rhoe, s=self.s , k=self.k, p0=self.p0)
        self.L  = self.Lq + self.s * self.rhoe
        self.W = lambda q : (self.L if q == '' else self.Lq)/self.lamdae
        
    # isErgodic
    def isErgodic(self):        
        return self.rho <1    
    
    # getStationaryProb
    def pn(self,n):
        pn0 = lambda n: self.s**min(self.s,n)/factorial(min(self.s,n)) * self.rho**n * self.p0        
        if n == 0 : return self.p0
        if self.k != -1 and n > self.k  : return 0
        return pn0(n)
    
    # show perforamnces
    def test(self):
        print('==================' + self.model + ' =======================')
        print("p0* :{:.5f}".format(self.p0))  
        print("p1* :{:.5f}".format(self.pn(1))) 
        print("Lq  :{:.2f}".format(self.Lq))  
        print("L   :{:.2f}".format(self.L))   
        print("W   :{:.2f}".format(self.W('')))
        print("Wq  :{:.2f}".format(self.W('q')))       
        
