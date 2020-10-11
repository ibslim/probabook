
    """
    sympy.stats
    FiniteRV(name, density)[source]

    Create a Finite Random Variable given a dict representing the density.
    Returns a RandomSymbol.
    """
    #   Examples
    from sympy.stats import FiniteRV, P, E
    density = {0: .1, 1: .2, 2: .3, 3: .4}
    X = FiniteRV('X', density)
    P(X >= 2)     #0.700000000000000
    .
    