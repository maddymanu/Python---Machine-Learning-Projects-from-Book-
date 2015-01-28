import requests 
import StringIO 
import numpy as np
import pandas as pd # pandas
import matplotlib.pyplot as plt # module for plotting 
import datetime as dt # module for manipulating dates and times
import numpy.linalg as lin # module for performing linear algebra operations

url_exprs = "https://raw.githubusercontent.com/cs109/2014_data/master/exprs_GSE5859.csv"
exprs = pd.read_csv(url_exprs, index_col=0)

url_sampleinfo = "https://raw.githubusercontent.com/cs109/2014_data/master/sampleinfo_GSE5859.csv"
sampleinfo = pd.read_csv(url_sampleinfo)

# print exprs.columns
# print sampleinfo.filename

# print sampleinfo[exprs.columns == sampleinfo.filename]

a = list(exprs.columns)
b = list(sampleinfo.filename)
matchIndex = [b.index(x) for x in a]
print matchIndex
exprs = exprs[matchIndex]

sampleinfo["date"] = pd.to_datetime(sampleinfo.date)
sampleinfo["month"] = map(lambda x: x.month, sampleinfo.date)
sampleinfo["year"] = map(lambda x: x.year, sampleinfo.date)

