
    """
    sympy.stats
    Die(name, sides=6)
    
    Create a Finite Random Variable representing a fair die. Returns a RandomSymbol.
    """
    #   Examples
    from sympy.stats import Die, density
    D6 = Die('D6', 6)               # Six sided Die
    ds6 = density(D6).dict      ;print(ds6) #{1:1/6,2:1/6,3:1/6,4:1   /6,5:1/6,6:1/6}
    D4 = Die('D4', 4)                       # Four sided Die
    ds4 = density(D4).dict      ;print(ds4) #{1:1/4,2:1/4,3:1/4,4:1/4}
    .
    
