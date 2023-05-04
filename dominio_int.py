# -*- coding: utf-8 -*-
"""
Questa funzione genera un insieme di numeri interi relativi compresi tra 
e1(incluso) ed e2(escluso), ad esclusione al massimo di un numero denominato 
'escludi'. 
Se non si vuole eliminare nessun numero dall'intervallo non inserire 'escludi' 

Parametri in input 
------------------
e1: int, estremo sinistro dell'intervallo, compreso nello stesso
e2: int, estremo destro dell'intervallo, non compreso nello stesso  
escludi: int, default=None, eventuale numero da escludere dall'intervallo

Output
------
list: se e1<e2, una sequenza di interi che parte da e1 incluso e si conclude
     con e2 escluso, eliminando al massimo un numero 'escludi' se compreso tra e1 ed e2   

oppure

str: 'dominio_vuoto', se e1>=e2

       
"""

def genera_dominio(e1: int, e2: int, escludi=None):#->list:
    if e1>=e2: 
        dominio="dominio_vuoto"
   # if type(e1)!=int or type(e2)!=int:  #in realta' non ci arriva qui, da' errore gia'nella riga di definizione
    #    print("Errore:e1 o e2 numeri non relativi, dominio vuoto")   #come far riconoscere TypeError: 'float' object cannot be interpreted as an integer
    else:
        dominio=list(range(e1,e2))
        if escludi is not None:
            if escludi in dominio:
                dominio.remove(escludi)
            else:
                print("Non e' possibile escludere", escludi, "dal dominio perche' non appartiene al dominio selezionato")
    return(dominio)

#print(genera_dominio(-3,3, 6))
#print(genera_dominio(3,3))
#print(genera_dominio(2.5, 3.1))
#print(genera_dominio(-3,3,1))
#print(type(genera_dominio(-3,3,1))) 
#print(genera_dominio(-9,9))
#print(len(genera_dominio(-9,9)))  
#print(genera_dominio(-2,2,0))
#print(len(genera_dominio(-2,2,0)))

#a=[1,3]
#a=3.5

print(genera_dominio(5,5))
print(type(genera_dominio(5,5)))    #-->da'correttamclass str ma perche' non da' errore se ho detto che deve essere una lista nella def?

a=genera_dominio(3, 6)
print(a)
print(type(a))

#controllare come fare se non voglionumeri relativi ma intervallo di reali o razionali
#controllare come escludere piu'di un valore
##test: genera_dominio(e,e)==dominio_vuoto 
##test: genera_dominio(e+1,e)==dominio_vuoto  oppure e1>=e2
##test: genera_dominio(e,e+1)==[e]
##test: genera_dominio[0]==e1???????
##test  assert escludi in dominio==False  --> se metto ""???
##test: len(genera dominio(e1,e2))==abs(e1-e2)   #e2 escluso
##test: len(genera dominio(e1,e2,escludi))==abs(e1-e2)-1     #e2 escluso
##test: len(genera dominio(e1,e2,escludi))==len(genera dominio(-e2,-e1,escludi))
##test: type(genera_dominio(e1,e2))==str    if e1>=e2
##test: type(genera_dominio(e1,e2))==list   if e1<e2
##test:(genera_dominio(2.5, 3.1))==TypeError
##test

###i test vanno rivisti se il dominio e'un intervallo di numeri reali