# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:38:02 2019

@author: SURESH
"""

import random

class Human(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gender = None
        self.bloodGroup = None
        self.height = None
        self.weight = None
        self.contactNo = None
        self.parents = None
        self.habit = None
        self.education = None
        self.address = None
        
    def get_age(self):
        return self.age
    def set_age(self, newage):
        self.age = newage
        
        
    def get_name(self):
        return self.name
    def set_name(self, newname=""):
        self.name = newname
        
        
    def get_gender(self):
        return self.gender
    def set_gender(self, gen = ""):
        self.gender = gen
        
        
    def get_bloodGroup(self):
        return self.bloodGroup
    def set_bloodGroup(self, bg):
        self.bloodGroup = bg
        
    def get_height(self):
        return self.height
    def set_height(self, ht):
        self.height = ht
        
    def get_weight(self):
        return self.weight
    def set_weight(self, wt):
        self.weight = wt
        
    def get_contactNo(self):
        return self.contactNo
    def set_contactNo(self, n):
        self.contactNo = n
        
    def get_parents(self):
        return self.parents
    def set_parents(self, p=""):
        self.parents = p
        
    def get_habbit(self):
        return self.habit
    def set_habbit(self, h=""):
        self.habit = h
        
    def get_education(self):
        return self.education
    def set_education(self, e=""):
        self.education = e
        
    def get_address(self):
        return self.address
    def set_address(self, a=""):
        self.address = a
        
    def __str__(self):
        return "Human : " + str(self.name) + " : "+ str(self.age)
    
    
class Student(Human):
    def __init__(self, name, age, college):
        Human.__init__(self, name,age)
        self.set_age(age)
        self.college = college
        self.type = None
        
    def get_college(self):
        return self.college
    def set_college(self, a=""):
        self.college = a
        
    def get_type(self):
        return self.type
    def set_type(self, a=""):
        self.type = a.capitalize()
        
    def __str__(self):
        return " Human->Student: <" + str(self.name) +":"+str(self.age)+"years old" +":"+str(self.college)+">"
    
    
#s1 = Student("sivaraman", 25, "IIT Madras")
#aa=s1.set_bloodGroup("A1 positive")
#
#
#print(s1, "is having blood group of", str(s1.get_bloodGroup()))

class IITian(Student):
    def __init__(self, name, age, college, department, professor = None):
        Student.__init__(self,name, age, college)
        self.department = department
        self.professor = professor
        
    def get_ProfName(self):
        return self.professor
    def set_ProfName(self, p =""):
        self.professor = p
        
    def set_Dept(self, p =""):
        self.department = p
    def get_Dept(self):
        return self.department
    
    def __str__(self):
        return " Human->Student -> IITians: <" + str(self.name) +":" \
    +str(self.age)+"years old" +":"+str(self.college)+':'+ str(self.department)+">"
    
i1 = IITian('Sivaraman',25,'IIT Madras', 'Ocean Engineering')
i1.set_Dept("Ocean Engineering")
i1.set_ProfName("Suresh Rajendran")

i2 = IITian("",24,"IIT Madras",'Ocean Engineering')
i2.set_Dept("Ocean Engineering")
i2.set_ProfName("Suresh Rajendran")

i3 = IITian("Paramesh",26,"IIT Madras",'Ocean Engineering')
i3.set_Dept("Ocean Engineering")
i3.set_ProfName("Suresh Rajendran")
#
print('\n', i1,'\n',i2, '\n', i3)
    
#n = int(input("Enter the required Number of  IIT students data Entry: "))

#assert n != 0

#Slist = []
#tn = n

#for i in range(n):
#    a = input("Enter the Name: ")
#    b = int(input("Enter the Age :"))
#    c = input("Enter the College: ")
#    d = input("Enter the Department Name:")
#    e = input("Enter the Professor's Name:")
#    
#    ss = IITian(a,b,c,d,e)
#    Slist.append(ss.__str__())

i1.set_bloodGroup("A1 positive")
i1.set_contactNo(9944244734)
i1.set_gender('male')
i1.set_height(179)
i1.set_weight(72)
i1.set_type("Engineering")


#print(Slist)

print(i1.get_name(), 'mobile number is registed as', i1.get_contactNo())
print("he belongs to", i1.get_type())
z = int(i1.get_weight())
y = int(i1.get_height())

print("BMI is calculated as", round( (z/(y/100)**2),3))



    
    
    

    
        
        
        
        
    
        

        
        
        

        
    
        
        
    
        
        
        
        
        
        
        