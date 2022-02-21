#Code401.py (Continuation)

    # is_irreducible
    def is_irreducible(self):
        return(nx.is_strongly_connected(makeGraf(self.S,self.P)[0])) 

