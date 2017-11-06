import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

rpoints=50.0
angpoints=200.0

R2=1
R=2.0
xdata=[]
ydata=[]
zdata=[]
x=[]
y=[]
z=[]
for r1 in xrange(int(rpoints)):
    for ang1 in xrange(int(angpoints)):
        r=R2*r1/rpoints
        ang=2*math.pi*ang1/angpoints
        x.append(r*math.sin(ang))
        y.append(r*math.cos(ang)*math.sin(2.0*ang-math.pi/2)+R*math.cos(2.0*ang))#+math.pi/2))
        z.append(r*math.cos(ang)*math.cos(2.0*ang-math.pi/2)+R*math.sin(2.0*ang))#+math.pi/2))
    xdata.append(x)
    x=[]
    ydata.append(y)
    y=[]
    zdata.append(z)
    z=[]

fig = plt.figure()
ax3D = fig.add_subplot(111, projection='3d')
ax3D.plot_surface(xdata,ydata,zdata)
ax3D.set_xlim3d(-R, R)
plt.show()
