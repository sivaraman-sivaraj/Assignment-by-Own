# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:07:24 2019

@author: Sivaraman Sivaraj
"""

class Aquabeings(object):
    def __init__(self, n, l, p):
        self.name = n
        self.life = l
        self.price = p
        
    def get_name(self):
        return self.name
    def get_life(self):
        return self.life
    def get_price(self):
        return self.price
    
    def VFM(self): #"""value for money = VFM"""
        return self.get_life() / self.get_price()
    
    def __str__(self):
        return self.name + " :  ₹ "+str(self.price)+"rupees, Life-"+str(self.life)
    
    
def Build_list(names, lifes, prices):
    
    group =[]
    
    for i in range(len(lifes)):
        group.append(Aquabeings(names[i],lifes[i],prices[i]))
        
    return group


def Greedy(lists, maxprice, keyFunction):
    
    listcopy = sorted(lists,key = keyFunction, reverse = True)
    
    result =[]
    
    totallife , totalprice = 0,0
    for i in range(len(listcopy)):
        if (totalprice + listcopy[i].get_price()  <= maxprice):
            result.append(listcopy[i])
            totallife += listcopy[i].get_life()
            totalprice += listcopy[i].get_price()
            
    return (result, totallife)

def testGreedy(lists, constraints, keyFunction): #constraint = maxlife#
    taken, life = Greedy(lists, constraints, keyFunction)
    print ("The expected amount life of aquabeings is", life)
    
    for fish in taken:
        print ("   ",fish)
        
def testGreedys(aquas, maximumcost):
    print ("optimized list based on life of aqua beings for ₹", maximumcost)
    
    testGreedy(aquas, maximumcost, Aquabeings.get_life)
    
    print ("optimized list based on price of aqua beings for ₹", maximumcost)
    
    testGreedy(aquas, maximumcost, lambda x:1/Aquabeings.get_price(x))
    
    print ("optimized list based on VFM(value for money) of aqua beings for ₹", maximumcost)
    
    testGreedy(aquas, maximumcost, Aquabeings.VFM)
    

names = ['jelly', 'gupfish', 'fighterfish', 'snakefish', 'tankfish',
         'seahorse', 'tortise', 'angel fish', 'goldfish', 'floran' ]

life = [24,6,60,48,100,24,500,5,8,24]
price = [1000,5,30,120,50,600,300,15,10,2000]

aquas = Build_list(names, life, price)

testGreedys(aquas, 3000)