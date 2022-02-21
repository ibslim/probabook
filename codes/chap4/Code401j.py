#Code401.py (Continuation)

    # steady state probabilities   
    def steady_prob(self):
        if(not self.is_ergodic()):return None
        n = len(self.S)
        A = np.vstack([self.P.T - np.identity(n),np.ones(n)])
        B = np.append(np.zeros(n),1)  
        return np.linalg.lstsq(A,B)[0]
