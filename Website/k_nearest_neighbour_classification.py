import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

n_neigh = 15

iris = datasets.load_iris()
x = iris.data[: , :2]

y = iris.target

print x.shape