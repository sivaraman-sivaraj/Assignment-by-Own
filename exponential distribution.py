# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 20:14:14 2019

@author: Sivaraman Sivaraj
"""

import matplotlib.pyplot as plt
import numpy as np
import math, time

start = time.time()
def expD(n,x,N):
    l =n*x
    factor1 = np.exp(-l)
    factor2 = (l**N)/(math.factorial(N))
    factor = factor1 * factor2
    return factor

def expSimulation(n,x,N):
    pv =[ ]
    Nvalues = [ ]
    p = 0
    while p < N:
        pv.append(p)
        cc = expD(n,x,p)
        Nvalues.append(cc)
        p +=1
    return (pv,Nvalues)

aa,ab = expSimulation(0.005,1000,100)

plt.figure(1)
plt.plot(aa,ab, label = "Exponential Distribution \n Curve", color = 'green')
plt.grid(True)
plt.legend(loc='best')
plt.xlabel("Number of Incidents")
plt.ylabel("Probablity")
plt.show()

end = time.time()
print("The time taken to run the codes is", round((end-start),5), "seconds")


























    
    
    