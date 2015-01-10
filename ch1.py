import scipy as sp
data = sp.genfromtxt("data/web_traffic.tsv", delimiter="\t")
print (data[:10])

# sha
print data.shape

x = data[:,0]
y = data[:,1]

print sp.sum(sp.isnan(y))

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

import matplotlib.pyplot as plt

plt.scatter(x,y)
plt.title("Web Traffic")
plt.xlabel("Time")
plt.ylabel("Gits/Hour")
plt.xticks([w*7*24 for w in range(10)] , ['week %i' %w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()

fx = sp.linspace(0,x[-1],1000) #generate x-values for plotting 
plt.plot(fx , f1(x) , linewidth=4)
plt.legend(["d=%i" % f1.order] , loc="upper left")

plt.show()
