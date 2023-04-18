# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:43:32 2023

@author: Matteo
"""

import array as arr
import numpy as np
import fz_genera_dominio_coeff

def assegna_abcd(dominio1, dominio2): 
    """Questa funzione assegna un valore random a 4 coefficienti 
        a, b, c, d nel seguente modo:
        """
    import random
    #abd_dominio = list(range(-9,10))
    #c_dominio= list(range(-9,10))
    #c_dominio.remove(0)
    #print( "il Dominio dei coefficienti a,b,d e\'", abd_dominio)
    #print( "il Dominio del coefficiente c e\'", c_dominio)
    print(dominio1)
    print(dominio2)
    a=random.choice(dominio1)       
    b=random.choice(dominio1)
    c=random.choice(dominio2)
    d=random.choice(dominio1)
    #print(a,b,c,d)
    return [a,b,c,d]

z=fz_genera_dominio_coeff.domini_abcd()
print(z)
w=assegna_abcd(fz_genera_dominio_coeff.domini_abcd())  #errore qui secondo arg

#coefficienti=assegna_abcd(fz_genera_dominio_coeff.domini_abcd())
#print('i coefficienti sono [a,b,c,d]=',coefficienti)
    
