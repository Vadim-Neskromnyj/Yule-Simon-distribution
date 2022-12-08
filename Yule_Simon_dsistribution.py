from scipy.stats import yulesimon 
import numpy as np
import matplotlib.pyplot as plt

f = open('distribution_help.txt')
line = f.readline()
while line:
    print (line),
    line = f.readline()
f.close()

numargs = yulesimon .numargs 
a, b = 0.2, 0.8
rv = yulesimon (a, b)
quantile = np.arange (0.01, 1, 0.1)

distribution = np.linspace(0, np.minimum(rv.dist.b, 10))
answer = input("Do you want to see distribution (yes, no): ")
if answer == "yes":
    print("Distribution : \n", distribution)

# Varying positional arguments
y1 = yulesimon.ppf(distribution, 1)
y2 = yulesimon.cdf(distribution, 0.05)

plt.xlim([0, 0.8])
plt.ylim([0, 5])
plt.plot(distribution, y1, label='Sine wave')
plt.show()

plt.xlim([1, 10])
plt.plot(distribution, y2, label='Cosine wave')
plt.show()