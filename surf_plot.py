import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import BoundaryNorm

xval = [i for i in np.arange(0,5,0.2)]
yval = [i for i in np.arange(0,5,0.2)]

x = []
y = []
z = []
for i in range(len(xval)):
    for j in range(len(yval)):
        x.append(xval[i])
        y.append(yval[j])
        z.append(np.cos(x[i])**2-np.sin(y[j]))

x = np.asarray(x)
y = np.asarray(y)
z = np.asarray(z)

##Evently spaced intervals in the axes
x1 = np.linspace(x.min(),x.max(),100)
y1 = np.linspace(y.min(),y.max(),100)
# VERY IMPORTANT, to tell matplotlib how is your data organized
z1 = griddata((x, y), z, (x1[None,:], y1[:,None]), method='cubic')



##color-map
palette = plt.cm.coolwarm
color_lev = [5*i/350 for i in range(70)]

##figure
fig = plt.figure(figsize=(18,20),dpi=50)
ax = fig.add_subplot(1,1,1, projection='3d')

x1g, y1g = np.meshgrid(x1, y1)
surf = ax.plot_surface(x1g, y1g, z1, rstride=1, cstride=2, linewidth=0, antialiased=True, cmap=palette, norm=BoundaryNorm(color_lev, ncolors=256, clip=False))

ax.set_xlabel("X",fontsize=20)
ax.set_ylabel("Y",fontsize=20)
ax.set_zlabel("Z",fontsize=20)

plt.show()
