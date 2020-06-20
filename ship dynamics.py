# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 09:14:40 2019

@author: Sivaraman Sivaraj
"""

class Ship_dynamics(object):
    def __init__(self, d, r, f,h):
        self.direction = d
        self.resistance = r
        self.fuelconsumption = f
        self.DesireFactor = h
        
    def get_direction(self):
        return self.direction
    def get_resistance(self):
        return self.resistance
    def get_dfactor(self):
        return self.DesireFactor
    def get_fuelconsumption(self):
        return self.fuelconsumption
    
    def VFF(self): #"""value for fuel = VFF"""
        return self.resistance() / self.fuelconsumption() 
    
    def __str__(self):
        return self.direction + " :  "+str(self.resistance)+"Newton/ meter^2, Fuel consumption-"+str(self.fuelconsumption)
    
    
def Build_list(direction, resistance, fuelconsumption, DesireFactor):
    
    group =[]
    
    for i in range(len(direction)):
        group.append(Ship_dynamics(direction[i],resistance[i],fuelconsumption[i]), DesireFactor[i])
        
    return group    

def Greedy(lists, maxfuel, keyFunction):
    
    listcopy = sorted(lists,key = keyFunction, reverse = True)
    
    result =[]
    
    totalrst , totalfuel = 0,0
    for i in range(len(listcopy)):
        if (totalfuel + listcopy[i].get_fuelconsumption()  <= maxfuel):
            result.append(listcopy[i])
            totalrst += listcopy[i].get_resistance()
            totalfuel += listcopy[i].get_fuelconsumption()
            
    return (result, totalrst)

def testGreedy(lists, constraints, keyFunction): #constraint = maxlife#
    taken, resis = Greedy(lists, constraints, keyFunction)
    print ("\n The expected amount of resistance born by ship is", resis)
    
    for dn in taken:
        print ("   ",dn)
        
def testGreedys(shipsd, maximumfuel):
    print ("/n optimized list based on minimum resistance on the ship for fuel consumption of ", maximumfuel)
    
    testGreedy(shipsd, maximumfuel, Ship_dynamics.get_resistance)
    
    print ("\n optimized list based on minimum fuel consumption by ship for fuel consumption of", maximumfuel)
    
    testGreedy(shipsd, maximumfuel, lambda x:1/Ship_dynamics.get_fuelconsumption(x))
    
    print ("\n optimized list based on VFF(value for fuel) for the fuel consumption of ", maximumfuel)
    
    testGreedy(shipsd, maximumfuel, Ship_dynamics.DesireFactor)
    
    
    
direction = ['North', ' South', 'East', 'West', 'North East','South East', 'South West', 
             'North West','North NorthEast','NorthEast East', 'East SouthEast', 
             'SouthEast South', 'South SouthWest', 'SouthWest West', 'NorthWest West', 
             'North NorthWest']

#print(len(direction))

resistance = [12,15,35,154,25,65,54,21,55,68,99,12,13,14,7,65]
    
#print(len(resistance))        

fuelconsumption = [2,6,545,21,25,35,15,65,65,84,95,65,16,32,15,11]

#print(len(fuelconsumption))

desireness = [10,10,2,8,6,4,5,7,8,9,6,5,4,2,5,6]
#print(len(desireness))

shipsd = Build_list(direction, resistance, fuelconsumption, desireness)
print(shipsd)

#testGreedys(shipsd, 600)









    