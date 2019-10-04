#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 12:18:20 2019

@author: scott
"""

# Create some functions that implement the logistic map
# Plot the map and orbits

# Logistic Map definition - alpha is the single parameter

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def logistic_map(x, alpha):
    l = alpha*x*(1-x)
    return l

def fun_iteration(fun, ntimes, **kwargs):
    got_alpha = False
    for k,v in kwargs.items():
        if k == "alpha":
            got_alpha = True
            alpha = v
    
    if got_alpha == True:
        print("Alpha value: {}".format(kwargs["alpha"]))
    else:
        print("No value for alpha supplied. Alpha assumed to be 1.")
        alpha = 1
    
    initial = np.random.rand(1)
    next_one = fun(initial, alpha = alpha)
    for n in range(ntimes):
        next_one = fun(next_one, alpha = alpha)
        print(next_one)
    
#fun_iteration(logistic_map, 200, alpha = 1.5)


def plot_orbit(start = 0.1, alpha = 1):
    
    x = np.arange(0,1,0.001)
    y= logistic_map(x, alpha = alpha)
    
    orb_x = []
    orb_y = []
    
    x_i = start
    
    for n in range(1000):
        
        if n % 2 == 0:
            orb_x.append(x_i)
            orb_y.append(x_i)
            y_i = logistic_map(x= x_i, alpha = alpha)
            
        else:
            orb_x.append(x_i)
            orb_y.append(y_i)
            x_i = y_i
      
    plt.close()
    plt.plot(x,x)
    plt.plot(x,y)
    plt.plot(orb_x, orb_y)
    plt.title("Logistic Map for alpha = {}".format(alpha))
    plt.show()
    

plot_orbit(alpha = 2.3)    
    
    
    



