# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:54:30 2020

@author:  Sivaraman Sivaraj

"""


#def f(x):
#    return x**2 + x + 2
#
list = [1,2,3,4,5]
#
ans =[]
#
#for i in map(f,list):
#    ans.append(i)
#    
#print(ans)



a = [i for i in range(100)]

#print(a)

b = [x+y+z for x in range(10) for y in range(10) for z in range(10) ]
print(b[:30])

hh=[]

for i in range(10):
    for j in range(10):
        for k in range(10):
            hh.append(i+j+k)
            
print(b[:30])
#for i in map(lambda x,y,z,a : (x**2+z*y*x+3), list, list,list,list):
#    ans.append(i)
#c=[1,2,3]
#d = [1,2,3]
#a = lambda x,y: x+y,c,d
#
#
#print(a)
#print(ans)
#    
    

import math, numpy as np, matplotlib.pyplot as plt, random

def f(x):
    return math.log(x)

x = np.arange(1,15)

y = [i for i in map(f,x)]

plt.scatter(x,y)
    


c=random.randint(0,10000)
print(c)



















