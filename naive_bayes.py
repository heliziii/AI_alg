import scipy.io
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


mat = scipy.io.loadmat('DataSet/Mnist/mnist_train.mat')
dataframe = pd.DataFrame(np.hstack((mat['X'], mat['Y'].T)))

names = list(map(str, range(65)))
dataframe.rename(columns= lambda x:str(x), inplace=True)
attribute_table = [[] for i in range(64)]


for i in range(64):
     x = dataframe.groupby([str(i),"64"]).size().reset_index(name = "time")
     attribute_table[i] = x.pivot(index=str(i), columns='64', values='time')
     attribute_table[i] = attribute_table[i].fillna(0)




test = scipy.io.loadmat('DataSet/Mnist/mnist_test.mat')
test_df = pd.DataFrame(np.hstack((test['X'],test['Y'].T)))


def maximum_liklihood(row,table,smoothing):
    max = 0
    index = 0
    for i in range(10):
        x = bayes(i,row,table,smoothing)
        if x > max:
            max = x
            index = i
    return index

def bayes(i,row,table,smoothing):
    P_xi = [0 for k in range(64)]
    for j in range(64):
        if table[j].index.contains(row[j]):
            P_xi[j] = table[j][i][row[j]]/ sum(table[j][i])
        else:
            P_xi[j] = smoothing
    mult = multi(P_xi)
    return mult * len(dataframe[dataframe['64'] == i]) / len(dataframe.index)



def multi(array):
    res = 1
    for i in array:
        res = res * i
    return res
result = [0 for i in range(540)]

for i in range(540):
    result[i] = maximum_liklihood(test_df.iloc[i],attribute_table,0)
print(confusion_matrix(result, test_df[64]))
print(accuracy_score(result, test_df[64]))

max = 0
index = 0
for j in range(1,6):
    counter = 0
    newTable = []
    for i in range(64):
        newTable.append(attribute_table[i] + j)
    for i in range(int(0.8 * len(dataframe.index)), len(dataframe.index)):
        if maximum_liklihood(dataframe.iloc[i],newTable,j) == dataframe['64'][i]:
            counter += 1
    if counter > max:
        max = counter
        index = j

print(index)
print(max)

for i in range(64):
    attribute_table[i] += index
for i in range(540):
    result[i] = maximum_liklihood(test_df.iloc[i],attribute_table,index)
print(confusion_matrix(result,test_df[64]))
print(accuracy_score(result, test_df[64]))
