# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:57:53 2019

@author: Sivaraman Sivaraj
"""
year=int(input("Enter the year: "))
month=int(input("enter the month: "))
date=int(input("enter the date: "))
if year%4 == 0:
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
        if date<31:
            print ("the exact next date will be")
            print (date+1,"/",month,"/",year)
        elif date==31:
            print ("the exact next date will be")
            print ("1/",month+1,"/",year)
        else:
            print ("enter the valid date please")
    elif month==4 or month==6 or month==9 or month==11:
        if date<30:
            print ("the exact next date will be")
            print (date+1,"/",month,"/",year)
        elif date==30:
            print ("the exact next date will be")
            print ("1/",month+1,"/",year)
        else:
            print ("enter the valid date please")
    elif month==12:
        if date<31:
            print ("the exact next date will be")
            print (date+1,"/",month,"/",year)
        elif date==31:
            print ("the exact next date will be")
            print ("1/1/",year+1)
        else:
            print ("enter the valid date please")
    elif month==2:
        if date<29:
            print ("the exact next date will be")
            print (date+1,"/",month,"/",year)
        elif date==29:
            print ("1/",month+1,"/",year)
        else:
            print ("enter the valid date please")
    else:
        print ("enter the valid month")
else:
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
        if date<31:
            print ("the exact next date will be")
            print (date+1,"/",month,"/",year)
        elif date==31:
            print ("the exact next date will be")
            print ("1/",month+1,"/",year)
        else:
            print ("enter the valid date please")
    elif month==4 or month==6 or month==9 or month==11:
        if date<30:
            print ("the exact next date will be")
            print (date+1,"/",month,"/",year)
        elif date==30:
            print ("the exact next date will be")
            print ("1/",month+1,"/",year)
        else:
            print ("enter the valid date please")
    elif month==12:
        if date<31:
            print ("the exact next date will be")
            print (date+1,"/",month,"/",year)
        elif date==31:
            print ("1/1/",year+1)
        else:
            print ("enter the valid date please")
    elif month==2:
        if date<28:
            print ("the exact next date will be")
            print (date+1,"/",month,"/",year)
        elif date==28:
            print ("1/",month+1,"/",year)
        else:
            print ("enter the valid date please")
    else:
        print ("enter the valid month")
