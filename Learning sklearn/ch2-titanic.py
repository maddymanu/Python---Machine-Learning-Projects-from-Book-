import csv
import numpy as np

with open('data/titanic.csv' , 'rb') as csvfile:
	titanic_reader = csv.reader(csvfile , delimiter=',' , quotechar='"')
	row = titanic_reader.next()
	feature_names = np.array(row)
	# print feature_names
	titanic_X , titanic_Y = [] , []

	for row in titanic_reader:
		titanic_X.append(row)
		titanic_Y.append(row[2])

	titanic_X = np.array(titanic_X)
	titanic_Y = np.array(titanic_Y)

print titanic_X[0] , titanic_Y[0]

titanic_X = titanic_X[:,[1,4,10]]
feature_names = feature_names[[1, 4, 10]]
print titanic_X[0]

