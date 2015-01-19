import csv
import IPython
import sklearn as sk
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pyparsing

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

# print titanic_X[0] , titanic_Y[0]

titanic_X = titanic_X[:,[1,4,10]]
feature_names = feature_names[[1, 4, 10]]
# print titanic_X[0]


ages = titanic_X[:, 1]
mean_age = np.mean(titanic_X[ages != 'NA', 1].astype(np.float))
titanic_X[titanic_X[:, 1] == 'NA', 1] = mean_age

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

enc = LabelEncoder()

label_encoder = enc.fit(titanic_X[: , 2])

print "Categorical classes:", label_encoder.classes_
integer_classes = label_encoder.transform(label_encoder.classes_)
print "Integer classes:", integer_classes
t = label_encoder.transform(titanic_X[:, 2])
titanic_X[:, 2] = t
print 'Features for instance number 12:',titanic_X[12], titanic_Y[12]

enc = LabelEncoder()
label_encoder = enc.fit(titanic_X[:, 0])
print "Categorical classes:", label_encoder.classes_
integer_classes = label_encoder.transform(label_encoder.classes_).reshape(3, 1)
print "Integer classes:", integer_classes
enc = OneHotEncoder()
one_hot_encoder = enc.fit(integer_classes)
# First, convert clases to 0-(N-1) integers using label_encoder
num_of_rows = titanic_X.shape[0]
t = label_encoder.transform(titanic_X[:, 0]).reshape(num_of_rows, 1)
# Second, create a sparse matrix with three columns, each one indicating if the instance belongs to the class
new_features = one_hot_encoder.transform(t)
# Add the new features to titanix_X
titanic_X = np.concatenate([titanic_X, new_features.toarray()], axis = 1)
#Eliminate converted columns
titanic_X = np.delete(titanic_X, [0], 1)
# Update feature names
feature_names = ['age', 'sex', 'first_class', 'second_class', 'third_class']
# Convert to numerical values
titanic_X = titanic_X.astype(float)
titanic_Y = titanic_Y.astype(float)



from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(titanic_X, titanic_Y, test_size=0.25, random_state=33)

from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3,min_samples_leaf=5)
clf = clf.fit(X_train,y_train)


# import StringIO
# dot_data = StringIO.StringIO() 
# tree.export_graphviz(clf, out_file=dot_data, feature_names=['age','sex','1st_class','2nd_class','3rd_class']) 
# graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
# graph.write_png('titanic.png') 
# from IPython.core.display import Image 
# Image(filename='titanic.png')





