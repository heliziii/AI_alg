from sklearn import tree
import pandas as pd
from sklearn.metrics import confusion_matrix

train_data = pd.read_csv('DataSet/Cancer/Train.txt', sep=",", header=None)
del train_data[0]
train_data[10].replace((4, 2), (1, 0), inplace=True)

train_data = train_data.fillna(train_data.mean())
clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data.iloc[:,0:9], train_data[10])


test_data = pd.read_csv('DataSet/Cancer/Test.txt', sep=",", header=None)
del test_data[0]
test_data[10].replace((4, 2), (1, 0), inplace=True)
test_data = test_data.fillna(test_data.mean())

result = clf.predict(test_data.iloc[:,0:9])

cm = confusion_matrix(result,test_data[10])
print(cm)

print(100 * (cm[0][0] + cm[1][1]) / (cm[0][1]+cm[1][0] + cm[0][0] + cm[1][1]))