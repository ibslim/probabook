import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


data = pd.read_csv('data.csv')  # load data set
X = data.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
Y = data.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class
m=linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X)  # make predictions
plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.show()
print("sklearn:  a=",m.intercept_, "  b=",m.coef_)
X=[X[i][0] for i in range(len(X))]
Y=[Y[i][0] for i in range(len(Y))]
Ex=np.mean(X)
Ey=np.mean(Y)
Vx=np.var(X)
Cov=np.cov(X,Y)[0][1]
b=Cov/Vx
a=Ey-Ex*b
print("Analytique: ""a=",a,"  b=",b)
predictedY=a+b*np.array(X)
plt.scatter(X, Y)
plt.plot(X, predictedY, color='red')
plt.show()
print('sklearn Mean squared error: %.2f'
      % mean_squared_error(Y, Y_pred))
print("Analytique Mean squared error:", mean_squared_error(Y, predictedY))
# The coefficient of determination: 1 is perfect prediction
print('sklearn Coefficient of determination: %.2f'
      % r2_score(Y, Y_pred))
print("Analytique Coefficient of determination:", r2_score(Y, predictedY))

# sklearn:  a= [9.90860619]   b= [[1.28735737]]
# Analytique: a= 9.263291199945208   b= 1.3004936697049203
# sklearn Mean squared error: 107.47
# Analytique Mean squared error: 107.4863522518873
# sklearn Coefficient of determination: 0.59
# Analytique Coefficient of determination: 0.5870998123555305

