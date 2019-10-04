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
    
fun_iteration(logistic_map, 200, alpha = 3.4)
