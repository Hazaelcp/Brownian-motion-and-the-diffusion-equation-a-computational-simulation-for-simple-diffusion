import numpy as np
import matplotlib.pylab as pl
import random 
from math import*
from mpl_toolkits.mplot3d import Axes3D
pl.style.use('dark_background')
n=30#numero de pasos en el tiempo 
fig=pl.figure()
ax=fig.add_subplot(111,projection='3d')

def grafi(k):
    k=k+0
    x = np.zeros(n) 
    y = np.zeros(n)
    z = np.zeros(n)

    sx=np.zeros(n)
    sy=np.zeros(n)
    sz=np.zeros(n)

    for i in range(1,n):
        x[i]=(np.random.rand()-0.5)* 2.
        y[i]=(np.random.rand()-0.5)* 2.
        z[i]=(np.random.rand()-0.5)* 2.


        sx[i]=x[i]+sx[i-1]
        sy[i]=y[i]+sy[i-1]
        sz[i]=z[i]+sz[i-1]

    ax.scatter(sx[n-1],sy[n-1],sz[n-1],'O',c='b')
    if k==1:
        ax.plot3D(sx,sy,sz,'g',linewidth=0.7)
for i in range(200):#numero de particulas
    grafi(0)

grafi(1)

x=np.arange(-int(sqrt(n)),int(sqrt(n)))
y=np.arange(-int(sqrt(n)),int(sqrt(n)))
z=np.arange(-int(sqrt(n)),int(sqrt(n)))

ax.scatter(0,0,0,'o',c='r')
pl.plot(x,y*0,z*0,'r',linewidth=0.5);pl.plot(x*0,y,z*0,'r',linewidth=0.5);pl.plot(x*0,y*0,z,'r',linewidth=0.5)
pl.grid(True,linewidth=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
pl.show()

