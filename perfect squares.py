

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:24:24 2019

@author: Sivaraman Sivaraj
"""
### exercise for finding the perfect squares in ranging numbers###
##hey there you go##
import pylab
#w = input("We are going to find the perfect squares inbetween any two integers. Are you ready?\n")
#if w == "yes" or w == "ok" or w == "Ok" or w == "s" or w == "ya":
#    print("\n let's start the game \n")
#else:
#    print("come on buddy. try once")
    
x=int(input("enter the starting value:\n"))
y=int(input("enter the ending value:\n"))
print("the perfect square numbers is/are")
svalues =[]
if x<y:
    for i in range (x,y+1):
        val=0
        while val**2<i:
            val = val+1
        if val**2 == i:
            svalues.append(val**2)    
    
elif y<x:
    for i in range (y,x-1):
        val=0
        while val**2<i:
            val = val+1
        if val**2 == i:
            svalues.append(val**2)
            
else:
    for i in range (x,y):
        val=0
        while val**2<i:
            val = val+1
        if val**2 == i:
            svalues.append(val**2)
            
pylab.plot(svalues, color='orange')   
pylab.title('Growth Figure of perfect squares', fontsize = 'x-large')
pylab.xlabel('Respective Terms')
pylab.ylabel('Perfect Squares')
pylab.savefig('Growth Figure of perfect squares')
    
print(" ###end of game##")

        