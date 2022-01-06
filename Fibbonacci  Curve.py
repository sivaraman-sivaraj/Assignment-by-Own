"""
Created on Thu Jan  6 09:47:54 2022

@author: Sivaraman Sivaraj
"""

import numpy as np
import matplotlib.pyplot as plt

def Fibbonacci(N):
    #################################################
    ########## Fibbonacci Numbers ###################
    #################################################
    F = [0,1]
    for i in range(N):
      F.append(F[-1]+F[-2])
    #################################################
    ############## Centroid Finder ##################
    #################################################
    I = [[0,0],[0,0],[0,0]]
    for j in range(3,N):
      pivot = (j-2)%4
      if pivot == 1:
        X_flag, Sign_Flag = True, True
      elif pivot == 2:
        X_flag, Sign_Flag = False, True
      elif pivot == 3:
        X_flag, Sign_Flag = True, False 
      elif pivot == 0:
        X_flag, Sign_Flag = False, False
      ############################################
      x_temp,y_temp = I[j-1][0], I[j-1][1]
      if Sign_Flag == True and X_flag == True:
        x_temp += F[j-2]
      elif Sign_Flag == True and X_flag == False:
        y_temp += F[j-2] 
      elif Sign_Flag == False and X_flag == True:
        x_temp -= F[j-2]
      elif Sign_Flag == False and X_flag == False:
        y_temp -= F[j-2]
      ##########################################
      I.append([x_temp,y_temp])
    ###############################################
    ############  Curve Formation #################
    ###############################################
    F,C   = F[1:], I[1:]
    P,X,Y  = [[0,0]],list(),list()
    Angle  = [[1,91],[91,181],[181,271],[271,361]] 
    for i in range(len(C)):
        ###  angle aliner ###
        pivot_a = i%4
        AnR     = Angle[pivot_a]
        r       = F[i]
        ### x,y alignment ###
        x_align, y_align = C[i][0],C[i][1]
        for j in range(AnR[0],AnR[1]):
            x_temp = r*np.cos(np.deg2rad(j))
            y_temp = r*np.sin(np.deg2rad(j))
            
            P.append([x_temp,y_temp])
            X.append(x_temp + x_align)
            Y.append(y_temp + y_align)
    ############################################
    ############  Length finder ################
    ############################################ 
    L = 0     
    for k in range(len(F)):
        r_temp = F[k]
        L += np.pi*(r_temp/2)
    return P,X,Y,L



P,X,Y,L = Fibbonacci(6)

plt.figure(figsize=(9,6))
plt.plot(X,Y)
plt.axhline(y=0,color ='k')
plt.axvline(x=0,color ='k')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Fibbonacci Curve")
plt.grid(which='major',linestyle='--')



