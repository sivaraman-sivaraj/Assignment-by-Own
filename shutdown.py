
"""
Created on Tue Jul 14 10:17:08 2020

@author: Sivaraman Sivaraj
"""

import os


def shutdown():
    rtn = os.system("shutdown /s /t 1")
    return rtn

# shutdown()



