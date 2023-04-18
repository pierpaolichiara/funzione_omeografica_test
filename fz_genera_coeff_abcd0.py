# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:43:32 2023

@author: Matteo
"""
import array as arr
import numpy as np

def assegna_abcd(): 
    """Questa funzione assegna un valore random a 4 coefficienti 
        a, b, c, d nel seguente modo:
        """
    import random
    abd_dominio = list(range(-9,10))
    c_dominio= list(range(-9,10))
    c_dominio.remove(0)
    print( "il Dominio dei coefficienti a,b,d e\'", abd_dominio)
    print( "il Dominio del coefficiente c e\'", c_dominio)
   
    a=random.choice(abd_dominio)        
    b=random.choice(abd_dominio)
    c=random.choice(c_dominio)
    d=random.choice(abd_dominio)
    #print(a,b,c,d)
    return [a,b,c,d]


#coefficienti=assegna_abcd(dominio1, dominio2)
coefficienti=assegna_abcd()
print('i coefficienti sono [a,b,c,d]=',coefficienti)
    
#funziona, domini nel corpo funzione