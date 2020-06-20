# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 01:03:10 2019

@author: Sivaraman Sivaraj
"""



N = int (input("How many numbers want to taking GCD: \n"))
L=[]

if N !=0:
    a = int(input("enter the 1st numerical value in integer: \n" ))
    L.append(a)
    
if N >1:
    
    b = int(input("enter the 2nd numerical value in integer: \n" ))
    L.append(b)
if N >2 :
    
    c = int(input("enter the 3rd numerical value in integer: \n" ))
    L.append(c)
        
if N>3:
    for i in range(3,N):
        x = int(input("enter the next numerical value in integer: \n"))
        L.append(x)
        
print("the LCM list is", L)      
        

def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    
    return result

def merge_sort(L):
    #print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
        
q = merge_sort(L)
print("The sorted version of List: \n",q)

def find_gcd(x, y): 
      
    while(y): 
        x, y = y, x % y 
      
    return x 
      

  
num1 = L[0] 
num2 = L[1] 
gcd = find_gcd(num1, num2) 
  
for i in range(2, len(L)): 
    gcd = find_gcd(gcd, L[i]) 
      
print("The Greatest Common dividend value is : ", gcd)

