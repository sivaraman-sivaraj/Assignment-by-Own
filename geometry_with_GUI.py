
"""
Created on Tue Oct 13 12:37:24 2020

@author: Sivaraman Sivaraj
"""


class square(object):
    """ 2D graphical things square, circle, triangle, rectangle, parallogram
    and romboid
    """
    def __init__(self,a):
        self.a=a
        
    def __str__(self):
        return "The size of square" + str(self.a)
    
    def area(self):
        
        area = (self.a)**2
        
        return "The area of square is "+ str(area)
    
    def perimeter(self):
        
        peri = 4*self.a
        
        return "The perimeter of square is " + str(peri)
    
    def diagonal(self):
        
        diag = (2**0.5)*self.a
        
        return "The length of diagonal is "+ str(diag)
    
    def moi(self):
        
        moi = (self.a**4)/12
        
        return "The moment of inertia of square is " +str( moi)
        
    
    
class hollow_square(object):
    
    def __init__(self,a1,a2):
        
        self.a1 = a1
        self.a2 = a2
        
        
    def __str__(self):
        return " The outer size is" + str(self.a1) + "\n The inner size is"+ str(self.a2)
    
    def area(self):
        
        area = (self.a1**2) - (self.a2**2)
        
        return "The area of hollow square is " + str(area)
    
    def perimeter(self):
        
        peri = (4*self.a1)+(4*self.a2)
        
        return "The perimeter of hollow square is " + str(peri)
    
    def dia_diff(self):
        
        l = (self.a1 - self.a2) * (2**0.5)
        
        return "The diagonal length is " + str(l)
    def moi(self):
        
        moi = ((self.a1**4)/12) - ((self.a2**4)/12)
        
        return "The area moment of inertia is " + str(moi)
    
    
class circle(object):
    def __init__(self,r):
        
        self.r = r
        
    def __str__(self):
        return "The radius of cirle is " + str(self.r)
    
    def area(self):
        pi = 3.14159
        area = pi*((self.r)**2)
        
        return "The area of circle is " + str(area)
    
    def circumference(self):
        pi = 3.14159
        cir = 2 * pi * self.r
        
        return "The circumference of circle is " + str(cir)
    def moi(self):
        pi = 3.14159
        moi = (pi/4)*(self.r **4)
        return "The area moment of inertia is " + str(moi)
    
        
    
class hollow_circle(object):
    
    def __init__ (self,r1,r2):
        
        self.r1 = r1
        self.r2 = r2
        
    def __str__(self):
        
        return " The Major radius is" + str(self.r1)+"\n The minor radius is"+ str(self.r2)
    
    
    def area(self):
        pi = 3.14159
        area = pi * ((self.r1**2)-(self.r2**2))
        
        return "The area of hollow circle is " + str(area)
    
    def circumference(self):
        
        pi = 3.14159
        cir = 2*pi*(self.r1 - self.r2)
        
        return "The circumfernce of hollow circle is " + str(cir)
    def moi(self):
        pi = 3.14159
        moi = (pi/4)*((self.r1 ** 4) - (self.r2**4))
        return "The area moment of inertia is "+ str(moi)
    
    
class rectangle(object):
    
    def __init__(self,l,b):
        self.l = l
        self.b = b
        
    def __str__(self):
        return "The length and breath of rectangle is" + str(self.l) + "," + str(self.b)
    
    
    def area(self):
        
        area = self.l* self.b
        
        return "The area of rectangle is "+ str(area)
    
    def perimeter(self):
        
        peri = (self.l + self.b)*2
        
        return "The perimeter of recangle is " + str(peri)
    
    def diagonal(self):
        
        dia = ((self.l ** 2) + (self.b **2))**0.5
        
        return "The lenth of diagonal is " + str(dia)
    
    def moi(self):
        
        moi = ((self.b) * (self.l ** 3))/12
        
        return "the area moment of inertia is " + str(moi)
    
class hollow_rectangle(object):
    
    def __init__(self,l1,b1,l2,b2):
        
        self.l1 = l1
        self.l2 = l2
        self.b1 = b1
        self.b2 = b2
        
    def __str__ (self):
        return "The Major length and breath of rectangle is " + str(self.l1)+","+str(self.b1)+"\n"+ "The minor length and breath of rectanlge is" + str(self.l2)+","+str(self.b2)
    
    
    def area(self):
        
        area = (self.l1 * self.b1) - (self.l2 * self.b2)
        
        return "The area of hollow rectangle is " + str(area)
    
    def perimeter(self):
        
        peri = ((self.l1 + self.b2) * 2) + ((self.l2 + self.b2) * 2)
        
        return "The perimeter of hollow rectangle is " + str(peri)
    
    def moi(self):
        moi = (((self.b1) * (self.l1 ** 3))/12) - (((self.b2) * (self.l2 ** 3))/12)
        return "The moment of inertia is " + str(moi)
        
        
class eqi_triangle(object):
    
    def __init__(self,a):
        self.a = a
      
    def area(self):
        area  = ((3**0.5)/4)*self.a
        
        return "The area of eqilatreal triangle is " + str(area)
    
    def centroid(self):
        
        c = ((self.a *2) - ((self.a)/2)*2) /3
        
        return "The hight of centroid from the base " + str( c)
    
    def perimeter(self):
        
        p = 3 * self.a
        return "The perimeter of euilatreal triangle is " + str(p)
    
    
class right_triangle(object):
    
    def __init__(self, b,h):
        
        self.b = b
        self.h = h
        
    def area(self):
        
        area = (self.b * self.h)/2
        
        return "The area of right angle triangle is " + str(area)
    
    def perimeter(self):
        
        peri = self.b + self.h +(((self.b **2)+(self.h **2))**0.5)
        
        return "The perimeter of right angle triangle is " + str(peri)
    
    
    
class general_triangle(object):
    
    def __init__(self,a,b,c):
        
        self.a = a
        self.b = b
        self.c = c
        
    def area(self):
        
        s = (self.a + self.b +self.c)/2
        
        area = ((s* (s - self.a) * (s- self.b) * (s- self.c))**0.5)

        return "The area of unequal triangle is " + str(area)
    
    def perimeter(self):
        
        p = self.a + self.b +self.c
        
        return "The perimeter of triangle is " + str( p)
    
class ellipse(object):
    
    def __init__(self,a,b):
        
        self.a =a
        self.b = b
        
    def area(self):
        
        pi = 3.14159
        area = pi * self.a * self.b
        return "The area of ellipse is " + str(area)
    
    def circumference(self):
        
        pi = 3.14159
        f = 0.5
        cir = pi*((3*(self.a + self.b)) - ((((3*self.a)+self.b))* ((self.a + (3*self.b)) )**f))
        return "The circumference of ellipse is " + str(cir)
    
    def moi(self):
        
        pi = 3.14159
        
        moi = (pi/4) *(self.a)*((self.b)**3)
        
        return "The moment of inertia about x-axis is " + str(moi)
    
    
    
    

import pyautogui

a = pyautogui.confirm("Tell which one, you would like to run?",
                        buttons=['1. Square',
                                 '2. Hollow Square',
                                 '3. Circle',
                                 '4. Hollow circle',
                                 '5. Rectangle',
                                 '6. Hollow Rectangle',
                                 '7. Eqi_Triangle',
                                 '8. Right angle triangle',
                                 '9. General triangle',
                                 '10. Ellipse'])




if(a== '1. Square'):
    
    r = pyautogui.prompt("Enter the Length of the Square \n")
    r = float(r)
    Square = square(r)
    pyautogui.alert(str(Square.perimeter()) +'\n'+ str(Square.area())+
                    '\n'+str(Square.diagonal())+'\n' + str(Square.moi()))
   
       
elif (a == '2. Hollow Square'):
    
    a1 = pyautogui.prompt("Enter the value of outer side: \n")
    a2 = pyautogui.prompt("Enter the value of inner side: \n")
    a1 = float(a1)
    a2 = float(a2)
    w =hollow_square(a1,a2)
    pyautogui.alert(str(w.area()) +'\n'+ str(w.perimeter())+
                    '\n'+str(w.dia_diff())+'\n' + str(w.moi()))
       
elif (a == '3. Circle'):
    
    r = pyautogui.prompt("Enter the value of radius: \n")
    r = float(r)
    w = circle(r)
    pyautogui.alert(str(w.area()) +'\n'+ str(w.circumference())+
                    '\n' + str(w.moi()))
    
    
elif (a == '4. Hollow circle'):
    
    r1 = pyautogui.prompt("Enter the value of outer radius: \n")
    r2 = pyautogui.prompt("Enter the value of inner radius: \n")
    r1,r2 = float(r1),float(r2)
    w = hollow_circle(r1, r2)
    
    pyautogui.alert(str(w.area()) +'\n'+ str(w.circumference())+
                    '\n' + str(w.moi()))
    

elif (a =='5. Rectangle'):
    
    l = pyautogui.prompt("Enter the value of length: \n")
    b = pyautogui.prompt("Enter the value of breadth: \n")
    l,b = float(l),float(b)
    w = rectangle(l,b)
    pyautogui.alert(str(w.perimeter()) +'\n'+ str(w.area())+
                    '\n'+str(w.diagonal())+'\n' + str(w.moi()))
    
    
elif (a == '6. Hollow Rectangle'):
    
    l1 = pyautogui.prompt("Enter the value of outer length: \n")
    b1 = pyautogui.prompt("Enter the value of outer breadth: \n")
    l2 = pyautogui.prompt("Enter the value of inner length: \n")
    b2 = pyautogui.prompt("Enter the value of inner breadth: \n")
    l1,l2,b1,b2 = float(l1),float(l2),float(b1),float(b2)
    assert l2 < l1 and b2 < b1
    
    w = hollow_rectangle(l1,b1,l2,b2)
    pyautogui.alert(str(w.perimeter()) +'\n'+ str(w.area())+
                    '\n' + str(w.moi()))       
    

elif (a== '7. Eqi_Triangle'):
    a = pyautogui.prompt("Enter the value of side length: \n")
    a = float(a)
    w = eqi_triangle(a)
    pyautogui.alert(str(w.perimeter()) +'\n'+ str(w.area())+
                    '\n' + str(w.centroid()))       
    
       
elif (a == '8. Right angle triangle'):
    
    b = pyautogui.prompt("Enter the value of base: \n")
    h = pyautogui.prompt("Enter the value of height: \n")
    b,h = float(b),float(h)
    w = right_triangle(b,h)
    pyautogui.alert(str(w.perimeter()) +'\n'+ str(w.area()))
    
     
elif (a == '9. General triangle'):
    
    a = pyautogui.prompt("Enter the value of side 1: \n")
    b = pyautogui.prompt("Enter the value of side 2: \n")
    c = pyautogui.prompt("Enter the value of side 3: \n")
    a,b,c = float(a),float(b),float(c)
    w = general_triangle(a,b,c)
    pyautogui.alert(str(w.perimeter()) +'\n'+ str(w.area()))
    
elif (a == '10. Ellipse'):
    
    a = pyautogui.prompt("Enter the value of major radius: \n")
    b = pyautogui.prompt("Enter the value of minor radius: \n")
    a,b = float(a),float(b)
    w = ellipse(a,b)
    
    pyautogui.alert(str(w.circumference()) +'\n'+ str(w.area())+
                    '\n' + str(w.moi()))   
    
    
else:
    print("Enter the valid input please")

    
    
    
    
    

    
       
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
        
    
    
    
    
    
