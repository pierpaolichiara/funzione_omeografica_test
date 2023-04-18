# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:43:32 2023

@author: Matteo
"""

import fz_genera_dominio_coeff

def assegna_abcd(dominio1, dominio2): 
    """Questa funzione assegna un valore random a 4 coefficienti 
        a, b, c, d nel seguente modo:
        """
    import random
    #abd_dominio = list(range(-9,10))
    #c_dominio= list(range(-9,10))
    #c_dominio.remove(0)
    print( "il Dominio dei coefficienti a,b,d e\'", dominio1)
    print( "il Dominio del coefficiente c e\'", dominio2)
    #dominio1, dominio2=domini_abcd
    #print(dominio1)
    #print(dominio2)
    a=random.choice(dominio1)        
    b=random.choice(dominio1)
    c=random.choice(dominio2)
    d=random.choice(dominio1)
    #print(a,b,c,d)
    return [a,b,c,d]

d1,d2=fz_genera_dominio_coeff.domini_abcd()
coefficienti=assegna_abcd(d1,d2)
#coefficienti=assegna_abcd(fz_genera_dominio_coeff.domini_abcd)
print('i coefficienti sono [a,b,c,d]=',coefficienti)
    
#funziona, domini come variabile, assegnati attraverso altra funzione