import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

rpoints=10.0
angpoints=100.0
R=50.0

x=[]
y=[]
z=[]

for r1 in xrange(int(rpoints)):
    for ang1 in xrange(int(angpoints)):
        r=50*r1/rpoints
        ang=2*math.pi*ang1/angpoints
        x.append(r*math.sin(ang))
        y.append(r*math.cos(ang)*math.sin(2.0*ang-math.pi/2)+R*math.cos(2.0*ang+math.pi/2))
        z.append(r*math.cos(ang)*math.cos(2.0*ang-math.pi/2)+R*math.sin(2.0*ang+math.pi/2))

fig = plt.figure()
ax3D = fig.add_subplot(111, projection='3d')
ax3D.scatter(x, y, z)

plt.show()
