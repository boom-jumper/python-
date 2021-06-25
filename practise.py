import matplotlib.pyplot as plt 
import math
import numpy as np 

theta = np.linspace(0, 2*math.pi, num=100)
r1 = [6 * math.sin(a) + 8 * math.cos(a) for a in theta]
r2 = [9 * math.sin(a) + 12 * math.cos(a) for a in theta]
r3 = [3 * math.sin(a) + 4 * math.cos(a) for a in theta]

plt.plot(theta, r1, theta, r2, theta, r3)
plt.show()
