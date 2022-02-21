#Code401.py (Continuation)

    # hitting_time : average time to hit for the first time the state given in the argument 
    def hitting_time(self,state):
        n, i = len(self.S), self.S.index(state)
        I = np.identity(n); I[i,i] = 0;   
        g = np.ones(n); g[i]=0;  
        for k in range(n):
            if(self.P[k,k] == 1): I[k,k], g[k] = 0, 0
        return np.matmul(np.linalg.inv(np.identity(n)-np.matmul(I,self.P)), g)
    
    
