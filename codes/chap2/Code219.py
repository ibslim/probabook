#Code219.py

import numpy as np
import matplotlib.pyplot as plt  

# sklinreg: performs linear regression using sklearn package 
def sklinreg(): 
    import pandas as pd                        # To read data
    from sklearn.linear_model import LinearRegression
    data = pd.read_csv('data.csv')             # load data set
    X = data.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
    Y = data.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
    linear_regressor = LinearRegression()      # create object for the class
    m=linear_regressor.fit(X, Y)               # perform linear regression
    Y_pred = linear_regressor.predict(X)       # make predictions
    return X,Y,m.intercept_[0],m.coef_[0][0],Y_pred

# analytic: performs linear regression using the results of the application
def analytic(X0,Y0):
    X=[X0[i][0] for i in range(len(X0))]
    Y=[Y0[i][0] for i in range(len(Y0))]
    Ex,Ey,Vx=np.mean(X),np.mean(Y),np.var(X)
    Cov=np.cov(X,Y)[0][1]
    b=Cov/Vx; a=Ey-Ex*b  
    predictedY=a+b*np.array(X)
    return a,b,predictedY

def plotter(X,Y,predictedY,col):
    plt.scatter(X, Y)
    plt.plot(X, predictedY, color=col)
    plt.show()

X,Y,ska,skb,skY_pred=sklinreg()
print("SKlearn results: a=",ska,"  b=",skb)

anala,analb,analY_pred=analytic(X,Y)
print("Analytic: ""a=",anala,"  b=",analb)

plotter(X,Y,skY_pred,'red')
plotter(X,Y,analY_pred,'green')

#______________________________   Output  ______________________________________
# SKlearn results: a= 9.908606190326537   b= 1.2873573700109313
# Analytic: a= 9.263291199945208   b= 1.3004936697049203