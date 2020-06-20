# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:35:13 2020

@author: Sivaraman Sivaraj

codes for brute force algorithm
"""

def BruteForce(list):
    complete_list = []
    for a in range(len(list)):
        B = [i for i in list]
        for aa in range(a):
            B = [t1+t2 for t1 in list for t2 in B]
        complete_list += B
    return complete_list


a = 'abcds'

s = BruteForce(a)

print(s)



