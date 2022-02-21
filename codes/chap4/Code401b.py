#Code401.py (Continuation)

    # classify
    def classify(self):
        graf, succ = makeGraf(self.S,self.P)
        cfcs=list(nx.strongly_connected_components(graf))
        classes={"transitoire":[],"reccurente":[]}
        for i in range(len(cfcs)):
            cfc , voisins = cfcs[i] ,set()
            for s in cfc: voisins = voisins|succ[s]-cfc
            classes["transitoire" if(len(voisins)>0) else "reccurente"].append(cfc) 
        return classes
