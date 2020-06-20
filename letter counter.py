# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:59:43 2019

@author: SURESH
"""

s = input("Enter the sentence for vowels check up: \n")
a=0
e=0
i=0
o=0
u=0
for char in s:
    
    if char == 'i' or char == 'I':
        i = i+1
        
    if char == 'u' or char == 'U':
        u = u+1
        
    if char == 'a' or char == 'A':
        a= a+1
        
    if char == 'e' or char == 'E':
        e = e+1
        
    if char == 'o' or char == 'I':
        o = o+1

if a >= 1:
    print("There is a letter 'A'\n", 'number of time appeared = ', a)
if e >= 1:
    print("There is a letter 'E'\n", 'number of time appeared = ', e)
if i >= 1:
    print("There is a letter 'I'\n", 'number of time appeared = ', i)
if o >= 1:
    print("There is a letter 'O'\n", 'number of time appeared = ', o)
if u >= 1:
    print("There is a letter 'U'\n", 'number of time appeared = ', u)
    
    
    
    