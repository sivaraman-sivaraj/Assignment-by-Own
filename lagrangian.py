# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:16:03 2020

@author: sivaraman sivaraj
"""

X= [3,4,5,6]
Y = [6,8,10,12]
#import random
#random.seed(42)
#for i in range(10):
#    tempy = random.randint(0,100)
#    Y.append(tempy)
#    
x = 5.999


def numerators(x,X):
    elements=[]
    num_values = []
    for i in range(len(X)):
        temp = (x-X[i])
        elements.append(temp)
    for i in range(len(X)):
        temp1 = elements[::]
        temp1.remove(temp1[i])
        numTemp = 1
        for i in range(len(temp1)):
            numTemp = numTemp*temp1[i]
        num_values.append(numTemp)
    return num_values

#print((numerators(x,X)))          
def denominators(X):
    element = 1
    den_values = []
    for i in range(len(X)):
        tempA = X[::]
        a = tempA[i]
        tempA.remove(a)
        for i in range(len(tempA)):
            element *= (a-tempA[i])
        den_values.append(round(element,4))
    return den_values
#print((denominators(X)))

def lagrangian(x,X,Y):
    num = numerators(x,X)
    den = denominators(X)
    temp = []
    for i in range(len(Y)):
        tempElement = (num[i]/den[i])*Y[i]
        temp.append(round(tempElement,3))
    sumans = 0
    for i in range(len(temp)):
        sumans += temp[i]
    
    return sumans

def Yvalue(x,X,Y,la):
    for i in range(len(X)):
        if x > X[i] and x < X[i+1]:
            b,a = Y[i], Y[i+1]
    if la>0:
        return a-la
    else:
        return b+la
    
 
    

la = lagrangian(x,X,Y) 
yv  = Yvalue(x,X,Y,la)


print("The corressponding Y value of", str(x),"is",yv)







  
