# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:26:06 2019

@author: Sivaraman Sivaraj
"""
##user gives range of numbers and dividend ... we have to find the summation series##
x=int(input("enter the value starting value:\n"))
y=int(input("enter the ending value:\n"))
z=int(input("enter the dividend value:\n"))

if x % z ==0:
    sum=0
    for i in range(x,y+1,z):
        sum +=i
    print("The summation value of the series whose elements can be diveded by",z," ranging from",x,"to",y,"is\n",sum)
elif x % z !=0:
    a= x%z
    vum=0
    for i in range(x+(z-a),y+1,z):
        vum +=i
    print("The summation value of the series whose elements can be diveded by",z," ranging from",x,"to",y,"is\n",vum)
else:
    print("inderminate form")