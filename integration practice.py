# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 22:14:12 2020

@author: ram arjunan
"""

import scipy.integrate as integrate
import numpy as np

import matplotlib.pyplot as plt

def linear(x):
    return x

def poly(x,a,b,c,d,e,f):
    return (a*x**5)+(b*x**4)+(c*x**3)+(d*x**2)+(e*x)+f


def log(x):
    return np.log(x)

N =5

def f(t, x):
    return np.exp(-x*t) / t**N


#aa = integrate.nquad(f, [[1, np.inf],[0, np.inf]])
#print(aa)
#
##aa=integrate.quad(poly,1.43,np.pi,args=(1,1,1,4,5,6))
##print(aa[0])
##    
#X = np.arange(0.1,10,0.1)
#Y = f(1,X)
##from scipy.integrate import simps
##simpsonValue = simps(Y,X)
##print(simpsonValue)
#
#plt.plot(X,Y)
##plt.ylim(-3,3)
##plt.xlim(-11,11)
#plt.show()
    



#from mpl_toolkits.mplot3d import axes3d
#from matplotlib import cm
#
#fig = plt.figure()
#ax = fig.gca(projection='3d')
#X = []
#for i in range(20):
#    X.append(np.random.randint(0,100))
#    
#    
#Y = np.arange(0,20,1)
#Z = [np.arange(0,10,0.5)]*20
#
##Plot contour curves
#cset = ax.contour(X, Y, Z, cmap=cm.coolwarm)
#
#ax.clabel(cset, fontsize=9, inline=1)
#
#plt.show()


#a,b,c = axes3d.get_test_data(0.05)
#print(len(c))

from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grab some test data.
#X, Y, Z = axes3d.get_test_data(0.05)

X,Y,Z = [],[],[]

for i in range(100):
    temp =[]
    for i in range(100):
        temp.append(np.random.randint(-30,30))
    X.append(temp)
#    
#
#for i in range(100):
#    temp =[]
#    for i in range(100):
#        temp.append(np.random.randint(-30,30))
#    Y.append(temp)   
#
#for i in range(100):
#    temp =[]
#    for i in range(100):
#        temp.append(np.random.randint(-30,30))
#    Z.append(temp)


# Plot a basic wireframe.
ax.plot_wireframe(X, X,X, rstride=10, cstride=10)

plt.show()













