import os 
import numpy as np 
import matplotlib.pyplot as plt 

def Prime_Numbers(n):
    PN = []
    for i in range(n):
        Flag = True
        
        for j in range(2,i):
            if (i%j) != 0:
                Flag = False
            else:
                Flag = True
                break
        if Flag == False:
            PN.append(i) 
    return PN 


Ns = Prime_Numbers(1000) 

def Numbers_to_lastString(A):
    N1,N3,N5,N7,N9 = 0,0,0,0,0
    for i in A:
        temp = int(str(i)[-1])
        if temp == 1:
            N1 += 1
        if temp == 3:
            N3 += 1
        if temp == 5:
            N5 += 1
        if temp == 7:
            N7 += 1
        if temp == 9:
            N9 += 1
    return [N1,N3,N7,N9] 

SS = Numbers_to_lastString(Prime_Numbers(100000))

x = np.array(["N1", "N3", "N7","N9"])
y = np.array(SS)
c = ['red', 'teal','blue', 'orange']

plt.figure(figsize=(9,6))
plt.bar(x,height = y, color = c)
plt.grid()
plt.show()
