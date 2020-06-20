
"""
Created on Wed Apr 29 13:18:37 2020

@author: ram arjunan
"""

"""
this file is about for correlation and regression

"""

import numpy as np


x = np.arange(1,100,2)
y = np.random.randint(-1000,1000, len(x))

# print("the value of x is",x)
# print("The value of y is", y)
##calculation of CoVariance##


def sumXY(x,y):
    ans = 0
    for i in range(len(x)):
        temp = x[i]*y[i]
        ans += temp
    return ans

def sumX(x):
    ans = 0
    for i in range(len(x)):
        temp = x[i]
        ans += temp
    return ans
    

def sumXsqrt(x):
    ans = 0
    for i in range(len(x)):
        temp = x[i] * x[i]
        ans += temp
    return ans


def covariance(x,y):
    temp1 = (sumXY(x, y) - ((sumX(x))*sumX(y)/(len(x)))) 
    temp2 = (1/len(x))
    ans = temp1*temp2
    return ans
    
def coeff_correlation(x,y):
    temp1 = (np.var(y) * np.var(x))**0.5
    temp2 = covariance(x,y)
    ans = temp2 / temp1
    
    return ans

def karl_person_coeff(x,y):
    num = sumXY(x, y) - ((sumX(x) * sumX(y))/len(x))
    den1 = ( sumXsqrt(x))**0.5
    den2 = sumXsqrt(x) / len(x)
    den3 = (sumXsqrt(y) - (sumXsqrt(y)/len(x)))**0.5
    
    ans = num / (den1 - (den2*den3))
    return ans

def stdError(x,y): #standard error by normal and karl correlation coefficient
    r1 = round(coeff_correlation(x, y),5)
    r2 = karl_person_coeff(x, y)
    n = len(x)**0.5
    
    se1 = (1-(r1**0.5))/n
    se2 = (1-(r2**0.5))/n
    return [se1,se2]

def limit_of_correlation(x,y):
    r = coeff_correlation(x, y)
    a,b = stdError(x, y)
    pe = 0.6745*a
    l1 = r + pe
    l2 = r - pe
    return [l1,l2]





print("The value of co-variance is",covariance(x, y))
print("The value of co-efficient of correlation is", coeff_correlation(x,y))
print("The standard error is", stdError(x, y))
print("limits of correlation co-effiecients ", limit_of_correlation(x, y))
    














