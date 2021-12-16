import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,10,15,20,25,30,35,40,45,50])
y = x**x
# Note that even in the OO-style, we use `.pyplot.figure` to create the
fig, ax = plt.subplots() # Create a figure and an axes.
#ax.plot(x, x, label='linear') # Plot some data on the axes.
#ax.plot(x, x**x, label='logn') # Plot more data on the axes...
#ax.plot(x, np.log10(x), label='cubic') # ... and some more.
#ax.plot(x,np.log10(x)*x)
#ax.plot(x,x**3,label='quadratic')
ax.plot(x,y,label='cubic')
print(y)
ax.set_xlabel('x label') # Add an x-label to the axes.
ax.set_ylabel('y label') # Add a y-label to the axes.
ax.set_title("Simple Plot") # Add a title to the axes.
ax.legend() # Add a legend.

def my_plotter():
    return plt.show()


my_plotter()