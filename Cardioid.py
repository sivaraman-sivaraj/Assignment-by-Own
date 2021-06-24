import numpy as np
import matplotlib.pyplot as plt

def f(a):
    X,Y = [],[]
    prp = []
    for i in range(0,-180,-1):
        x = 2*a*(1-np.cos(np.deg2rad(i)))*np.cos(np.deg2rad(i))
        y = 2*a*(1-np.cos(np.deg2rad(i)))*np.sin(np.deg2rad(i))
        X.append(x)
        Y.append(y)
        prp.append([x,y])
        
    for i in range(180,0,-1):
        x = 2*a*(1-np.cos(np.deg2rad(i)))*np.cos(np.deg2rad(i))
        y = 2*a*(1-np.cos(np.deg2rad(i)))*np.sin(np.deg2rad(i))
        X.append(x)
        Y.append(y)
        prp.append([x,y])
        
    prp_new = []
    for j in range(len(prp)):
        temp = prp[-j]
        prp_new.append(temp)
        
    return prp_new,X,Y



def f2(a):
    X,Y = [],[]
    prp = []
    for i in range(0,-180,-1):
        x = 2*a*(1-np.cos(np.deg2rad(i)))*np.cos(np.deg2rad(i))*np.cos(np.deg2rad(i))
        y = 2*a*(1-np.cos(np.deg2rad(i)))*np.sin(np.deg2rad(i))
        X.append(x)
        Y.append(y)
        prp.append([x,y])
        
    for i in range(180,0,-1):
        x = 2*a*(1-np.cos(np.deg2rad(i)))*np.cos(np.deg2rad(i))*np.cos(np.deg2rad(i))
        y = 2*a*(1-np.cos(np.deg2rad(i)))*np.sin(np.deg2rad(i))
        X.append(x)
        Y.append(y)
        prp.append([x,y])
        
    return prp,X,Y


def f3(a):
    X,Y = [],[]
    prp = []
    for i in range(-180,180):
        x = 2*a*(np.sin(np.deg2rad(i)))*(a**np.cos(np.deg2rad(i)))
        y = 2*a*(np.cos(np.deg2rad(i)))*(a**np.sin(np.deg2rad(i)))
        X.append(x)
        Y.append(y)
        prp.append([x,y])
        
    return prp,X,Y


def f4(a):
    X,Y = [],[]
    prp = []
    for i in range(-180,180):
        x = 2*a*(np.sin(i)*(a**np.cos(np.deg2rad(i))))
        y = 2*a*(np.cos(i)*(a**np.sin(np.deg2rad(i))))
        X.append(x)
        Y.append(y)
        prp.append([x,y])
    return prp,X,Y


p,a,b = f3(20)


plt.figure(figsize=(6,6))
plt.plot(a,b,'r') #label="Nishi : I am very simple \n meanwhile her lifestyle"
plt.fill(a,b,color='red',alpha=0.25)
plt.xlabel("$\pi ---->$  in radian")
plt.ylabel("$\psi  ---->$ in radian")
plt.title("Parametric Curve")
plt.grid()
# plt.legend(loc="best")
plt.axhline(y = 0,color='k')
plt.axvline(x = 0,color='k')
plt.show()





