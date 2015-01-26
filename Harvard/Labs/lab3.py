import pandas as pd
import matplotlib.pyplot as plt


pd.options.display.mpl_style = 'default'

import numpy as np
from numpy import random
import pylab

# x = np.array([1,2,3,4])
# print x

# print np.arange(1,10,2)


# print np.random.randint(5,7,5)

# z = np.random.rand(4,4)
# print z

import scipy

from scipy import stats
from scipy.stats import norm


url = 'https://raw.githubusercontent.com/cs109/2014_data/master/mtcars.csv'
mtcars = pd.read_csv(url, sep = ',', index_col=0)
print mtcars.head()

print (mtcars > 0).any()

x = np.arange(0, 5, 0.1)
y = np.sin(x)

plt.plot(x , y)
# plt.xlim(3, 9)
# plt.xlabel('Cylinders')
# plt.ylabel('MPG')
# plt.title('Relationship between cylinders and MPG')
pylab.show()
