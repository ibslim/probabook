#Code401.py (Continuation)

    # absorption probability 
    def absorbing_proba(self,state):
        n, j = len(self.S) , self.S.index(state)
        absorb = [i for i in range(n) if(self.P[i][i] == 1) ]
        if(j not in absorb):
            print("The state must be absorbant")
            sys.exit(0)        
        A, B = np.zeros((n,n)), np.zeros(n)
        A[j][j], B[j] = 1 , 1
        for i in range(n):
            if(i != j):
                if(i in absorb): A[i][i] = 1
                else:
                    for k in range(n):
                        A[i][k] = self.P[i][k] if(k != i) else A[i][i]-1
        return np.linalg.inv(A).dot(B)
