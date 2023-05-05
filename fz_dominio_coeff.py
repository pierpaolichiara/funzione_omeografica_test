# -*- coding: utf-8 -*-
"""
   Questa funzione restituisce una sequenza di 4 coefficienti interi [a,b,c,d] appartenenti all'intervallo di interi [e1,e2),
   generandoli come segue:
   - a,b,c,d vengono scelti random con la funzione random.choice all'interno di [e1,e2) 
   - vengono controllate le condizioni necessarie (C.N.) per l'esistenza di una funzione omeografica propria f(x)=(a*x+b)/(c*x+d)
   associata alla quaterna dei coefficienti selezionati, che sono
 
   C.N.1:  c≠0 
   
   C.N.2:  a*d-c*b≠0
   
   Qualora almeno una delle due C.N. non sia rispettata, viene generata una 
   nuova sequenza di coefficienti e ricontrollate le C.N. fino a quando entrambe risultano verificate 
 
   Parametri in input
   ------------------
   e1: int, estremo sinistro dell'intervallo, compreso nello stesso
   e2: int, estremo destro dell'intervallo, non compreso nello stesso 
 
   Output
   -------
   [a,b,c,d]: list 
       sequenza di 4 coefficienti interi appartenenti al dominio di interi [e1,e2) 
 
   Raises ###??? TRADUZIONE?
   ------
   -Se vengono inseriti estremo sinistro >= dell'estremo destro (se e1>=e2):      
       il Dominio dei coefficienti a,b,c,d e' []                                #???inserire questa riga?
       IndexError: list index out of range
   -Se vengono inseriti float invece che int come estremi:
       TypeError: 'float' object cannot be interpreted as an integer
     
 
   Vedi anche
   ----------
#TODO    random.choice 
"""
import random

def assegna_abcd_omeo(e1:int, e2:int)->list: 
    dominio=list(range(e1,e2))
    print( "il Dominio dei coefficienti a,b,c,d e\'", dominio)  #??ha senso stamparlo?non e'nel return
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
                                    #???se nel return non cé il dominio non lo posso controllare
e1,e2=5,3

abcd=assegna_abcd_omeo(e1,e2)
#print(type(abcd))
#print('i coefficienti sono [a,b,c,d]=',abcd)
    
#funziona, domini come variabile, assegnati attraverso altra funzione
#!!!random.seed da inserire non qui ma nella fz he genera i coefficienti per 
#tutta la classe, altrimenti tutti i ragazzi avranno stesso vettore

##test:
#    c=0
#delta=0
#len(abcd)=4    
#e1<=a,b,c,d<=e2
#se metto dominio nel return posso fare test di dominio_int.py