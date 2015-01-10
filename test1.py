import numpy as np

a = np.array([0,1,2,3,4,5])
print a

print a.ndim

b = a.reshape((3,2)).copy()
print b

b[1][0] = 55
print b


print a

print a**2