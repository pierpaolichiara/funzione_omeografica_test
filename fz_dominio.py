# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 15:37:40 2023

@author: Matteo
"""

import numpy as np
import array

def dominio(Min: int, Max: int, elimina:int, type):
    dom=(Min, Max, elimina, type) 
    #dominio[coeff]=range(Min,Max)
    #dominio[coeff].remove(elimina)
    #print(dominio[coeff])
    #return(dominio[coeff], dominio[coeff].dtype )
    return dom


A=dominio(-9,10,0,int)
print(A)
