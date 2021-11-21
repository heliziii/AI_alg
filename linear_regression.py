import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


train_data = pd.read_csv('DataSet/weather/weather_train.csv')

X = train_data.iloc[:,:6]
Y = train_data.iloc[:,6]
m = len(train_data.index)
ones = np.ones(m).T
X.insert(0,"ones",ones)

tetas = np.matmul(np.linalg.inv((np.matmul(X.transpose(),X))),X.transpose()).dot(Y)

print("coefficients for the first part", tetas)

test_data = pd.read_csv('DataSet/weather/weather_test.csv')
X_test = test_data.iloc[:,:6]
Y_test = test_data.iloc[:,6]
ones = np.ones(len(test_data.index)).T
X_test.insert(0,"ones",ones)


MSE = ((X_test.dot(tetas.T) - Y_test)**2).mean()


print("mean square error for the first part", MSE)


landas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
new_X = X.iloc[0:int(m*0.8)]
new_Y = Y.iloc[0:int(m*0.8)]
min = 100000000
chosen_landa = 0

for i in landas:
    w = np.matmul(np.linalg.inv((np.matmul(new_X.transpose(),new_X)) + i * 7 * np.identity(7)),new_X.transpose()).dot(new_Y)
    MSE = ((X.iloc[int(m*0.8):].dot(w) - Y.iloc[int(m*0.8):]) ** 2).mean()
    print("error for lambda: ",i," = " , MSE)
    if MSE < min:
        min = MSE
        chosen_landa = i

w = np.matmul(np.linalg.inv((np.matmul(X.transpose(),X)) + chosen_landa * 7 * np.identity(7)),X.transpose()).dot(Y)
print("chosen lambda" ,chosen_landa)
print("coefficients for the second part",w)
print("mean square error for the second part",((X_test.dot(w) - Y_test)**2).mean())
