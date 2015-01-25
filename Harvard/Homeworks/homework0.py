import numpy as np

x = np.random.random((3, 4))
# print x

# print x[1, 2]



# print x[0 , ::2]

print x.max(axis=1)
print x.min()
print x.mean()

"""
Function
--------
simulate_prizedoor

Generate a random array of 0s, 1s, and 2s, representing
hiding a prize between door 0, door 1, and door 2

Parameters
----------
nsim : int
    The number of simulations to run

Returns
-------
sims : array
    Random array of 0s, 1s, and 2s

Example
-------
>>> print simulate_prizedoor(3)
array([0, 0, 2])
"""
def simulate_prizedoor(nsim):
    answer = np.random.randint(0,3, nsim)
    print answer
    return answer
#your code here

# simulate_prizedoor(3)

def simulate_guess(nsim):
	ans = np.zeros(nsim, dtype=np.int)
	print ans
	return ans


simulate_guess(5)













# end

