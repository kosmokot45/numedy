import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#x-axis ranges from -3 and 3 with .001 steps
x = np.arange (-3, 3, 0.001)

#plot normal distribution with mean 0 and standard deviation 1
plt.plot(x, norm.pdf(x, 0, 1))