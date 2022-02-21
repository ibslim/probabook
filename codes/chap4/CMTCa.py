#CMTC.py (Continuation)

# hitting_time : average time to hit for the first time the state given in the argument 
def hitting_time(self,state):
    i = self.S.index(state)
    I = np.identity(len(self.S)-1);   
    lambdas_inv = np.delete(np.reciprocal(self.Q.diagonal()),i)
    PK = np.delete(np.delete(self.P,i,0),i,1)
    return -np.matmul(np.linalg.inv(I-PK), lambdas_inv)
