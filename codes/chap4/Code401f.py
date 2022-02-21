#Code401.py (Continuation)

    # return_time : average return time to the state given in the argument 
    def return_time(self,state):
        i = self.S.index(state)
        return 1 + ( 0 if self.P[i,i] == 1 else  np.dot(self.P[i], self.hitting_time(state)))

