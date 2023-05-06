# -*- coding: utf-8 -*-
"""
Questa funzione restituisce una sequenza random di 4 coefficienti interi [a,b,c,d] 
appartenenti al dominio indicato in input, che verificano le condizioni necessarie per generare una funzione omeografica propria.

I coefficienti vengono scelti random con la funzione random.choice della libreria random, applicata alla sequenza in ingresso.

Vengono controllate le condizioni necessarie (C.N.) per l'esistenza di una funzione omeografica propria f(x)=(a*x+b)/(c*x+d)
associata alla quaterna dei coefficienti selezionati, che sono
 
   C.N.1:  c≠0 
   
   C.N.2:  a*d-c*b≠0
   
Qualora almeno una delle due C.N. non sia rispettata, viene generata una 
nuova sequenza di coefficienti e ricontrollate le C.N. fino a quando entrambe risultano verificate 
 
Parametri in input
------------------
dominio: list, insieme di interi da cui estrarre a, b, c, d
 
Output
-------
[a,b,c,d]: list 
    sequenza di 4 coefficienti interi appartenenti a dominio in input, idonei a generare una funzione omeografica propria 
 
Raises ###??? TRADUZIONE?
------
 
 
Vedi anche
----------
#TODO    random.choice 
dominio_int.genera_dominio

"""

import dominio_int
import random

def assegna_abcd_omeo(dominio: list)->list():
    c=0
    while c==0:			#verifica C.N.1
    	c=random.choice(dominio)
    delta=0
    while delta==0:                 #verifica C.N.2
       	a=random.choice(dominio)        
       	b=random.choice(dominio)
       	d=random.choice(dominio)
       	delta=a*d-c*b
    print('[a,b,c,d] = ', [a,b,c,d])    #???TOGLIERE?
    return [a,b,c,d]

dominio=dominio_int.genera_dominio(-9,10,1)  
abcd=assegna_abcd_omeo(dominio)
#print(abcd)
print('i coefficienti sono [a,b,c,d]=',abcd)
    
#funziona, domini come variabile, assegnati attraverso altra funzione
#!!!random.seed da inserire non qui ma nella fz he genera i coefficienti per 
#tutta la classe, altrimenti tutti i ragazzi avranno stesso vettore
