import numpy as np
import matplotlib.pylab as pl
import random 
from math import*
from statistics import mean
pl.style.use('dark_background')
n=1000
t=np.arange(n)
xaux=np.zeros(n)
x=np.zeros(n)
for i in range(1,n):
    xaux[i]=np.random.uniform(-1,1)
    x[i]=xaux[i]+x[i-1]

pl.plot(t,x,'y',linewidth=0.7)
pl.grid(True,linewidth=0.5)
pl.xlabel("t")
pl.ylabel("x")
pl.show()


ns=30#numero de simulaciones por cantidad de tiempo 

def brow1d(n):
    x=np.zeros(n)
    xaux=np.zeros(n)
    for i in range(1,n):
        xaux[i]=np.random.uniform(-1,1)
        x[i]=xaux[i]+x[i-1]
    return (x[n-1])

def vesp(n):
    lista=[]
    for i in range(ns):
        lista.append(abs(brow1d(n)))
    p=(mean(lista))**2
    return p*2

def einstein(k):
    lista=np.zeros(k)
    t=np.arange(k)

    for i in range(k):
        lista[i]=vesp(i+1)
    
    pl.plot(t,lista,'X')
    pl.grid(True)
    pl.xlabel("t")
    pl.ylabel("DCM")
    pl.show()

einstein(100)#numero de particulas simuladas 


    
        