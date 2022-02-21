    import pykov;  import networkx as nx
    
    #
    p = {('A','A'): 1, ('B','A'): 1/3, ('B','C'): 2/3,('C','B'): 1/2,('C','D'): 1/2,('D','D'): 1}
    T = pykov.Chain(p); print(T.states())
    p = pykov.Vector(C=1)
    print(T.pow(p,3))
    print(p*T*T*T)
    
    #
    G = nx.DiGraph(list(T.keys()))
    
    print(nx.is_strongly_connected(G))
    print(nx.is_aperiodic(G))
    print(list(nx.strongly_connected_components(G)))
    #
    s = {'B', 'C'}
    tau = T.absorbing_time(s)
    print(tau)
