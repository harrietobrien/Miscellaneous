#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 18:07:17 2019

@author: harrietobrien
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def plot(k,c):
    
    v = np.arange(0,1500,0.1)
    
    v_max_O2_298 = v_max(k,298,32*c)
    v_max_N2_298 = v_max(k,298,28*c)
    v_max_O2_1273 = v_max(k,1273,32*c)
    v_max_N2_1273 = v_max(k,1273,28*c)
    
    f_O2_298 = func(v,v_max_O2_298,298)
    f_N2_298 = func(v,v_max_N2_298,298)
    f_O2_1273 = func(v,v_max_O2_1273,1273)
    f_N2_1273 = func(v,v_max_N2_1273,1273)
    
    plt.plot(v,f_O2_298,f_N2_298)

def func(v,v_max,T):
    return ((4/math.sqrt(math.pi))*(v**2)*
            ((1/v_max)**3)*(math.e**((-v**2)/v_max**2)))

def v_max(k,T,m):
    return (math.sqrt(2*k*T/m))

    
if __name__ == '__main__':
    k = 1.38*10**(-23)
    c = 1.66*10**(-27) 
    plot(k,c)
    

