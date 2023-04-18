# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 12:40:13 2023

@author: Matteo
"""

#import numpy as np

def domini_abcd():
    abd_dominio = list(range(-9,10))
    c_dominio= list(range(-9,10))
    c_dominio.remove(0)
    print( "il Dominio dei coefficienti a,b,d e\'", abd_dominio)
    print( "il Dominio del coefficiente c e\'", c_dominio)
    return(abd_dominio, c_dominio)
 
domini_abcd()