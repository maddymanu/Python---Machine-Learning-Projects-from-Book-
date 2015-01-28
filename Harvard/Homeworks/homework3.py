import requests 
import StringIO
import zipfile
import numpy as np
import pandas as pd # pandas
import matplotlib.pyplot as plt # module for plotting 

# If this module is not already installed, you may need to install it. 
# You can do this by typing 'pip install seaborn' in the command line
# import seaborn as sns 

import sklearn
import sklearn.datasets
import sklearn.cross_validation
import sklearn.decomposition
import sklearn.grid_search
import sklearn.neighbors
import sklearn.metrics

# teams = pd.read_csv('data/Teams.csv')

# players = pd.read_csv('data/Batting.csv')

# salaries = pd.read_csv('data/Salaries.csv')

# fielding = pd.read_csv('data/Fielding.csv')

# master = pd.read_csv('data/Master.csv')
# # print teams.head()

# byPlayerID = salaries.groupby('playerID')['playerID','salary'].median()
# medianSalaries = pd.merge(master[['playerID', 'nameFirst', 'nameLast']], byPlayerID, \
#                   left_on='playerID', right_index = True, how="inner")
# # print medianSalaries.head()


# subTeams = teams[(teams['G'] == 162) & (teams['yearID'] > 1947)].copy()
# # print subTeams.head()

# subTeams["1B"] = subTeams.H - subTeams["2B"] - subTeams["3B"] - subTeams["HR"]
# subTeams["PA"] = subTeams.BB + subTeams.AB

# for col in ["1B","2B","3B","HR","BB"]:
#     subTeams[col] = subTeams[col]/subTeams.PA
    
# stats = subTeams[["teamID","yearID","W","1B","2B","3B","HR","BB"]].copy()
# print stats.head()



# for col in ["1B","2B","3B","HR","BB"]:
#     plt.scatter(stats.yearID, stats[col], c="g", alpha=0.5)
#     plt.title(col)
#     plt.xlabel('Year')
#     plt.ylabel('Rate')
#     plt.show()



#load the iris data set
iris = sklearn.datasets.load_iris()

X = iris.data  
Y = iris.target

print X.shape, Y.shape



















