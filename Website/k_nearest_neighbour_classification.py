import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

n_neigh = 15

iris = datasets.load_iris()
x = iris.data[: , :2]

y = iris.target

print x.shape

h = 0.02

cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

for weights in ['uniform' , 'distance']:
	clf = neighbors.KNeighborsClassifier(n_neigh , weights = weights)

	x_min = x[: , 0].min()-1
	x_max = x[: , 0].max()+1

	y_min = x[: , 1].min()-1
	y_max = x[: , 1].max()+1

	xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

