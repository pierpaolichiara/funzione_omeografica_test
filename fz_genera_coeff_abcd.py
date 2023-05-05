# -*- coding: utf-8 -*-
"""
Questa funzione assegna un valore random a 4 coefficienti 
a, b, c, d nel seguente modo: 
- a,b,d vengono scelti random con la funzione random.choice da dominio1
- c viene scelto random con la funzione random.choice da dominio2
- viene calcolato 

    delta = a*d-c*b 
    
- viene verificata la condizione

    delta=0
    
  come C.N. per avere una quaterna di coefficienti utili a generare una funzione omeografica. 
  Qualora la C.N. non sia verificata, viene generata e verificata una nuova quaterna di coefficienti 
  
Parametri in input
------------------
  dominio1: list, insieme di interi di appartenenza da cui estrarre a, b, d
  dominio2: list, insieme di interi di appartenenza da cui estrarre c
  
Output
-------
  [a,b,c,d]: list 
      sequenza di 4 coefficienti interi appartenenti ai domini in input:
          a,b,d ϵ dominio1
          c ϵ dominio2
      
Raises ###??? TRADUZIONE?
------
##TODO   Se dominio1 o dominio2 sono str, cioe' se vengono inseriti 
 estremo sinistro >= dell'estremo destro:      

 TypeError: unsupported operand type(s) for -: 'int' and 'str':
 TypeError: can't multiply sequence by non-int of type 'str'    
 
Vedi anche
----------
#TODO    random.choice    
"""

import dominio_int

def assegna_abcd(dominio1: list, dominio2: list): 
    import random
    print( "il Dominio dei coefficienti a,b,d e\'", dominio1)
    print( "il Dominio del coefficiente c e\'", dominio2)
    delta=0
    while delta==0:                 #verifica C.N.2
        a=random.choice(dominio1)        
        b=random.choice(dominio1)
        c=random.choice(dominio2)
        d=random.choice(dominio1)
        delta=a*d-c*b
    print('[a,b,c,d] = ', [a,b,c,d])
    return [a,b,c,d]

d_abd=dominio_int.genera_dominio(-9,10)  
d_c=dominio_int.genera_dominio(-9,10,0)

#print(type(d_c))


abcd=assegna_abcd(d_abd,d_c)
#print(type(abcd))
#print('i coefficienti sono [a,b,c,d]=',abcd)
    
#funziona, domini come variabile, assegnati attraverso altra funzione
#!!!random.seed da inserire non qui ma nella fz he genera i coefficienti per 
#tutta la classe, altrimenti tutti i ragazzi avranno stesso vettore