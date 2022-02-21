#Code303.py

import numpy as np
import matplotlib.pyplot as plt

# poisson_Proc: generates sampling for Poisson SP for different parameters
def poisson_Proc(N,lambdas):
    X_T = [np.random.poisson(lam, size=N) for lam in lambdas]
    return [np.cumsum(X) for X in X_T]

def plot_Poisson(N,S,lambdas):
    X = np.linspace(0, N, N)
    G = [plt.step(X, S[i], label="Lambda = %d"%lambdas[i])[0] for i in range(len(lambdas))]
    plt.legend(handles=G, loc=2)
    plt.title("Poisson Process", fontdict={'fontname': 'Times New Roman', 'fontsize': 21}, y=1.03)
    plt.ylim(0);  plt.xlim(0)
    plt.show()

N , lambdas = 20 , [4, 7, 13]
S = poisson_Proc(N,lambdas)
plot_Poisson(N,S,lambdas)

    
    