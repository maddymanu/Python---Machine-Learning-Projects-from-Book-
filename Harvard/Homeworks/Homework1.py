import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


salaries = pd.read_csv('data/Salaries.csv' , sep=',')
# print salaries.head()

teams = pd.read_csv('data/Teams.csv' , sep=',')
# print teams.head()

salaries = salaries.groupby(['yearID' , 'teamID'] , as_index=False).sum()
# print salaries

mergedDF = pd.merge(salaries , teams , how='inner' , on=['yearID' , 'teamID'])
# print mergedDF.head()


teamName = "OAK"
years = np.arange(2000 , 2004)
print years

print mergedDF['yearID']

for yr in years:
	df = mergedDF[mergedDF['yearID'] == yr]
	print df
	plt.scatter(df['salary'] / 1e6 , df['W'])
	plt.title('Wins versus Salaries in year ' + str(yr))
    # plt.xlabel('sss')
    # plt.ylabel('Wins')
	plt.xlim(0, 180)
	plt.ylim(30, 130)
	plt.grid()
	plt.annotate(teamName, 
        xy = (df['salary'][df['teamID'] == teamName] / 1e6,  df['W'][df['teamID'] == teamName]), 
        xytext = (-20, 20), textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', facecolor = 'black' , connectionstyle = 'arc3,rad=0'))
	plt.show()
