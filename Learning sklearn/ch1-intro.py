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


from sklearn.linear_model import SGDClassifier
clf = SGDClassifier()
clf.fit(X_train, Y_train)

plt.legend(iris.target_names)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')


import numpy as np

x_min, x_max = X_train[:, 0].min() - .5, X_train[:, 0].max() + .5
y_min, y_max = X_train[:, 1].min() - .5, X_train[:, 1].max() + .5

xs = np.arange(x_min,x_max,0.5)

fig, axes = plt.subplots(1, 3)
fig.set_size_inches(10, 6)

import pylab

for i in [0, 1, 2]:
	axes[i].set_aspect('equal')
	axes[i].set_title('Class '+ str(i) + ' versus the rest')
	axes[i].set_xlabel('Sepal length')
	axes[i].set_ylabel('Sepal width')
	axes[i].set_xlim(x_min, x_max)
	axes[i].set_ylim(y_min, y_max)
	pylab.sca(axes[i])
	plt.scatter(X_train[:, 0], X_train[:, 1], c=Y_train,
           cmap=plt.cm.prism)
	ys = (-clf.intercept_[i]-xs*clf.coef_[i,0])/clf.coef_[i,1]
	plt.plot(xs, ys, hold=True)


plt.show()





