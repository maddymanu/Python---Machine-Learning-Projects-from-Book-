url = 'https://raw.githubusercontent.com/cs109/2014_data/master/diamonds.csv'


import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.mpl_style = 'default'

diamonds = pd.read_csv(url , sep=',' , index_col=0)
# print diamonds.head()

# print diamonds.describe()

# diamonds['price'].hist(bins=50, color = 'black')
# plt.title('Distribution of Price')
# plt.xlabel('Price')

# print diamonds.mean()

subtitles = diamonds[0:2]
print subtitles

color = diamonds['color'][1]
print "color of diamond in row 1"
print color
print ""