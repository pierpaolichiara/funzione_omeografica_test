# -*- coding: utf-8 -*-
"""
Questa funzione genera un insieme di numeri relativi compresi tra e1(incluso) 
ed e2(escluso), ad esclusione al massimo di un numero Elimina. 

Se non si vuole eliminare nessun numero dall'intervallo: 
    digitare "" al posto di elimina
"""

def genera_dominio(e1,e2,Elimina):
    if e1>=e2:
        print("Errore:dominio vuoto")
    if type(e1)!=int or type(e2)!=int:
        print("Errore:e1 o e2 numeri non relativi, dominio vuoto")   #come far riconoscere TypeError: 'float' object cannot be interpreted as an integer
    dominio=list(range(e1,e2))
    if Elimina in dominio:
        dominio.remove(Elimina)
    return(dominio)

#print(genera_dominio(5,5,""))
#print(genera_dominio(-4,5,""))
print(genera_dominio(-9,9,""))
print(len(genera_dominio(-9,9,"")))  
print(genera_dominio(-2,2,0))
print(len(genera_dominio(-2,2,0)))
#controllare come fare se non voglionumeri relativi ma intervallo di reali o razionali
#controllare come escludere piu'di un valore
##test: genera_dominio(e,e,"")==[] 
##test: genera_dominio(e+1,e,"")==[]  oppure e1>=e2
##test: genera_dominio(e,e+1,"")==[e]
##test: genera_dominio[0]==e1
##test  assert Elimina in dominio==False  --> se metto ""?
##test: len(genera dominio(e1,e2,""))==abs(e1-e2)   #e2 escluso
##test: len(genera dominio(e1,e2,Elimina))==abs(e1-e2)-1     #e2 escluso
##test: len(genera dominio(e1,e2,Elimina))==len(genera dominio(-e2,-e1,Elimina))