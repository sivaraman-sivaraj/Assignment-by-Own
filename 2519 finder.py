# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:52:45 2019

@author: Sivaraman Sivaraj
"""

import time
start = time.time()


x = 9

flag = True

while(flag):

	for i in range(2,11):

		if(x%i!=i-1):
	
			flag = False		
			break

	if(flag):

		break

	flag = True

	x = x + 10	


print(x)

end = time.time()

print("time required to run the 1st code", start-end)

s = time.time()

q = 1
while q>0:
    if q%10 == 0 and q%9 == 0 and q%8 == 0 and q%7 == 0 and q%6 == 0 \
        and q%5 == 0 and q%4 == 0 and q%3 == 0 and q%2 == 0:
        
        print(q -1)
        break
    q = q +1
e = time.time()

print("time required to run the 2nd code", e-s)








