import pandas as pd
import numpy
from sklearn.metrics import confusion_matrix


train_data = pd.read_csv('DataSet/Cancer/Train.txt', sep=",", header=None)
del train_data[0]
train_data[10].replace((4, 2), (1, 0), inplace=True)
train_data = train_data.fillna(train_data.mean())

def logistic_regression(X, Y, n, rate,thetas):
    X = numpy.hstack((numpy.ones((X.shape[0], 1)), X))
    for i in range(n):
        Z = X.dot(thetas)
        new_Y = 1 / (1 + numpy.exp(-Z))
        delta = Y - new_Y
        grad = (X.T).dot(delta)
        thetas += rate * grad
    return thetas


thetas = [0 for i in range(10)]

thetas = logistic_regression(train_data.iloc[:,0:9],  train_data[10], 3000, 1e-5,thetas)

print(thetas)

test_data = pd.read_csv('DataSet/Cancer/Test.txt', sep=",", header=None)
del test_data[0]
test_data[10].replace((4, 2), (1, 0), inplace=True)
test_data = test_data.fillna(test_data.mean())

X_test = numpy.hstack((numpy.ones((test_data.iloc[:,0:9].shape[0], 1)), test_data.iloc[:,0:9]))
Y_test = numpy.round(1 / (1 + numpy.exp(-X_test.dot(thetas))))

cm = confusion_matrix(test_data[10],Y_test)
print(cm)

print(100 * (cm[0][0] + cm[1][1]) / (cm[0][1]+cm[1][0] + cm[0][0] + cm[1][1]))