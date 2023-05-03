# -*- coding: utf-8 -*-
"""
Questa funzione genera un insieme di numeri interi relativi compresi tra 
e1(incluso) ed e2(escluso), ad esclusione al massimo di un numero denominato 
'escludi'. 

Se non si vuole eliminare nessun numero dall'intervallo: 

Parametri    

"""

def genera_dominio(e1: int, e2: int, escludi=None)->list:
    if e1>=e2:                          
        return(print("dominio vuoto"))
   # if type(e1)!=int or type(e2)!=int:  #in realta' non ci arriva qui, da' errore gia'nella riga di definizione
    #    print("Errore:e1 o e2 numeri non relativi, dominio vuoto")   #come far riconoscere TypeError: 'float' object cannot be interpreted as an integer
    else:
        dominio=list(range(e1,e2))
        if escludi is not None:
            if escludi in dominio:
                dominio.remove(escludi)
            else:
                print("il numero", escludi, "da escludere non appartiene al dominio selezionato")
        return(dominio)
    return()

#print(genera_dominio(-3,3, 6))
print(genera_dominio(3,3))
        

#print(genera_dominio(2.5, 3.1))

#print(type(genera_dominio(-3,3,1))) 
#print(genera_dominio(-9,9))
#print(len(genera_dominio(-9,9)))  
#print(genera_dominio(-2,2,0))
#print(len(genera_dominio(-2,2,0)))

#print(genera_dominio(5, 3))  #sistemarereturn None lo prende come return della def
#print(genera_dominio(5,5))
#print(genera_dominio(-4,5))
#controllare come fare se non voglionumeri relativi ma intervallo di reali o razionali
#controllare come escludere piu'di un valore
##test: genera_dominio(e,e)==[] 
##test: genera_dominio(e+1,e)==[]  oppure e1>=e2
##test: genera_dominio(e,e+1)==[e]
##test: genera_dominio[0]==e1
##test  assert escludi in dominio==False  --> se metto ""?
##test: len(genera dominio(e1,e2))==abs(e1-e2)   #e2 escluso
##test: len(genera dominio(e1,e2,escludi))==abs(e1-e2)-1     #e2 escluso
##test: len(genera dominio(e1,e2,escludi))==len(genera dominio(-e2,-e1,escludi))