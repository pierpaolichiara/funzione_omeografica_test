# -*- coding: utf-8 -*-
"""

"""
import dominio_int

def assegna_abcd(dominio: list): 
    import random
    c=0
    while c==0:			#verifica C.N.1
    	c=random.choice(dominio)
    delta=0
    while delta==0:                 #verifica C.N.2
       	a=random.choice(dominio)        
       	b=random.choice(dominio)
       	d=random.choice(dominio)
       	delta=a*d-c*b
    print('[a,b,c,d] = ', [a,b,c,d])
    return [a,b,c,d]

dominio=dominio_int.genera_dominio(-9,10)  

#print(type(d_c))

abcd=assegna_abcd(dominio)
#print(type(abcd))
#print('i coefficienti sono [a,b,c,d]=',abcd)
    
#funziona, domini come variabile, assegnati attraverso altra funzione
#!!!random.seed da inserire non qui ma nella fz he genera i coefficienti per 
#tutta la classe, altrimenti tutti i ragazzi avranno stesso vettore
