# utils.py (Continuation)

# sort_PDF: returns a key sorted distribution of the argument  
def sort_PDF(prob_RV):
    return {key:prob_RV[key] for key in sorted(prob_RV.keys())}

# zip : create an iterator that aggregate a collection's elements
# map : applies a function to the elements of a list. 
# create_FiniteRV: Create a distribution by mapping a function on Omega's elements
def create_FiniteRV(Omega, map_X):
    return dict(zip(Omega, map(map_X, Omega)))
        
# get_InversedFiniteRV: inverses a finite RV distribution (value:key)
def get_InversedFiniteRV(finiteRV):
    return {v:{i for i in finiteRV.keys() if finiteRV[i] == v } for k,v in finiteRV.items()}
        
# get_PMF: returns the probability distribution P_X of X 
def get_PMF(finiteRV, probability_Omega):
    inv_X =  get_InversedFiniteRV(finiteRV)            
    prob_values = list(map(sum,
        [[probability_Omega[omega] for omega in event] for event in inv_X.values()]))
    return dict(zip(inv_X.keys(), prob_values))
    
# accumulate : returns the reduced result by applying the given operation on a set 
# get_CDF: cumulative distribution function CDF of X
def get_CDF(prob_RV):
    sprob_RV =sort_PDF(prob_RV)# {key:prob_RV[key] for key in sorted(prob_RV.keys())}
    return sprob_RV,dict(zip(sprob_RV.keys(), list(accumulate(sprob_RV.values()))))
    
# plot_Pdf_Cdf: plots PDF and CDF of RV X
def plot_Pdf_Cdf(pdf0, cdf0, choice =None):
    first  = list(pdf0.keys())[0]
    last   = list(pdf0.keys())[-1]
    keys   = [first-1] + list(pdf0.keys()) + [last+1]
    pvalues = [0.0]+ list(pdf0.values())
    
    fig = plt.figure()
    ncols0 =  2 if choice == None else 1
    axes = fig.subplots(nrows=1, ncols=ncols0)
    axes[0].bar(keys, pvalues + [0.0], width=0.05)

    if not choice:
        cvalues = [0.0]+ list(cdf0.values())
        axes[1].step(keys, [0.0]+ cvalues)
        
    plt.show()    


