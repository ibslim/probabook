#Code502.py

from Code501 import Queueing

# getMM1
def getMM1(lamda, mu):
    #
    laws ={
    'MM1' : {
        'p0' : lambda **p: (1 - p['rho1']),                          # p0 = 1 - rho,
        'Lq' : lambda **p: p['rho1'] / (1 - p['rho1']) - p['rho1'],  # Lq = L - rho
        },
    }
    
    #=========================================================================
    # Tests
    qs = Queueing(
            model = 'MM1', 
            A ={'D':'Pois' , 'params': { 'lambda': lamda}},
            B ={'D':'Expo' , 'params': { 'mu': mu}},
            laws = laws)
    qs.test()


if __name__ == "__main__":  getMM1(4,6)
# ==================MM1 =======================
# p0* :0.33333
# p1* :0.22222
# Lq  :1.33
# L   :2.00
# W   :0.50
# Wq  :0.33