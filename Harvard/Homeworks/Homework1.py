import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import requests
import StringIO
import zipfile
import scipy.stats 

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
# print years

# print mergedDF['yearID']

# for yr in years:
# 	df = mergedDF[mergedDF['yearID'] == yr]
# 	print df
# 	plt.scatter(df['salary'] / 1e6 , df['W'])
# 	plt.title('Wins versus Salaries in year ' + str(yr))
#     # plt.xlabel('sss')
#     # plt.ylabel('Wins')
# 	plt.xlim(0, 180)
# 	plt.ylim(30, 130)
# 	plt.grid()
# 	plt.annotate(teamName, 
#         xy = (df['salary'][df['teamID'] == teamName] / 1e6,  df['W'][df['teamID'] == teamName]), 
#         xytext = (-20, 20), textcoords = 'offset points', ha = 'right', va = 'bottom',
#         bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
#         arrowprops = dict(arrowstyle = '->', facecolor = 'black' , connectionstyle = 'arc3,rad=0'))
	# plt.show()


url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
s = StringIO.StringIO(requests.get(url).content)
countries = pd.read_csv(s , sep=',')
# print countries.head()


income_link = 'https://spreadsheets.google.com/pub?key=phAwcNAVuyj1jiMAkmq1iMg&output=xls'
source = StringIO.StringIO(requests.get(income_link).content)
income = pd.read_excel(source , sheetname='Data')
print income.head()

income.index = income[income.columns[0]]
income = income.drop(income.columns[0] , axis=1)
income.columns = map(lambda x: int(x), income.columns)
income = income.transpose()
print income.head()

year=2000
# plt.plot(subplots=True)
# plt.hist(income.ix[year].dropna().values , bins=20)
# plt.title('Year: %i' % year)
# plt.xlabel('Income per person')
# plt.ylabel('Frequency')
# plt.show()



def mergeByYear(year):
	data = pd.DataFrame(income.ix[year].values , columns=['Income'])
	# print data.head()
	data['Country'] = income.columns
	joined = pd.merge(data , countries , how="inner" , on=['Country'])
	joined.Income = np.round(joined.Income, 2)
	return joined 




print mergeByYear(2010).head()









