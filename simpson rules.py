# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 07:32:18 2020

@author: Sivaraman Sivaraj
"""
import numpy as np
import datetime, time, random, math
import matplotlib.pyplot as plt

h = 0.1 #step size
Y = [3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

def simpson13Integration(h,Y):
    term1 = (Y[0]+Y[len(Y)-1])
    term2 = 0
    for i in range(1,len(Y)):
        term2 += Y[i]
    ans =(h/3)*(term1 + (2*term2))
    return ans

aa = simpson13Integration(h,Y)
print("The value of integration by simpson 1/3 rule is", aa)

def simpson38Integration(h,Y):
    term1 = (Y[0]+Y[(len(Y))-1])
    term2 = 0#summation of odd element
    for i in range(1,len(Y),2):
        term2 += Y[i]
    term3 = 0#summation of even element
    for i in range(2,len(Y),2):
        term3 += Y[i]
    ans = (3*h/8)*(term1+(4*term2)+(2*term3))
    return ans    

ab = simpson38Integration(h,Y)
print("The value of integration by simpson 3/8 rule is", ab)

plt.figure()
X = np.arange(0,(h*len(Y)),h)
plt.plot(X,Y,'r')
plt.scatter(X,Y, marker='^')
plt.show()













  




#simpson 1/3 ruke