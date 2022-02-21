#Code401.py (Continuation)

    # average absorption time
    def absorbing_time(self):
        n = len(self.S)
        absorb = [i  for i in range(n) if(self.P[i][i] == 1)]
        if(len(absorb) == 0):
            print("No absorbant state exists!")
            sys.exit(0)
        A, B = np.zeros((n,n)), np.zeros(n)
        for i in range(n):
            if(i in absorb): A[i][i]=1
            else:
                B[i] = -1
                for j in range(n):
                    if(j not in absorb): A[i][j]=self.P[i][j]
                A[i][i] -= 1
        return np.linalg.inv(A).dot(B)
