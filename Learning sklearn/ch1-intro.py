from sklearn import datasets
iris = datasets.load_iris()

X_iris , Y_iris = iris.data , iris.target

from sklearn.cross_validation import train_test_split
from sklearn import preprocessing

print X_iris , "the Data itself"

X, y = X_iris[:, :2], Y_iris

print X , "Onlu the first 2 colums on the data"

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.25, random_state=33)

scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

print X_train , "Sclaed data"

import matplotlib.pyplot as plt
colors = ['red', 'greenyellow', 'blue']
for i in xrange(len(colors)):
	xs = X_train[: , 0][Y_train==i]
	ys = X_train[: , 1][Y_train==i]
	plt.scatter(xs , ys , c=colors[i])

plt.legend(iris.target_names)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()