import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0,9,1)
y = np.log10(np.arange(0,9,1))

line=plt.plot(x,y)
plt.setp(line, color='g')
plt.show()

"""# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()"""