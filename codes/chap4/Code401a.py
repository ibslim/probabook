#Code401.py (Continuation)

    # nSteps probabilities
    def nSteps(self,n):
        return self.pi0.dot(np.linalg.matrix_power(self.P,n))
