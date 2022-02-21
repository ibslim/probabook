    import pykov; import networkx as nx
    
    d = {('R', 'N'): 1/3, ('R', 'S'): 1/3, ('S', 'R'): 3/4,
         ('R', 'R'): 1/3, ('N', 'S'): 2/5, ('S', 'S'): 1/8,
         ('S', 'N'): 1/8, ('N', 'R'): 3/5, ('N', 'N'): 0}
    T = pykov.Chain(d); print(T.states())
    p = pykov.Vector(R=1)

    #
    G = nx.DiGraph(list(T.keys()))
    print(nx.is_strongly_connected(G))
    print(nx.is_aperiodic(G))
    print(T.steady())
    print(T.mfpt_to('R'))
