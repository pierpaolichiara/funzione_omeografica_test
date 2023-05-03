""" 
Progetto per docenti di matematica delle scuole secondarie superiori:
Questo programma e' pensato per produrre test a risposta aperta sulla funzione 
omeografica f(x)=(ax +b)/(cx+d) da somministrare a una classe di studenti.
Ogni coefficiente della funzione viene scelto in maniera casuale all'interno 
di un dominio da specificare. A ogni alunno il programma associa una quaterna 
di coefficienti [a,b,c,d] diversa, e per ogni alunno stampa il testo del test #in formato...##. 
L'associazione tra cognome dell'alunno e quaterna di coefficienti viene 
stampata su un file excel disponibile per l'insegnante

"""

import numpy as np
from numpy import random
from random import random
import sympy as sp
from sympy import symbols
import funzione_omeografica




import array as arr

a,b,c,d=1,3,5,7
parametri=arr.array('i',[a,b,c,d])
abcd=[a,b,c,d]
print (parametri)
print(abcd)
y=funzione_omeografica.genera_fz_omeografica(a,b,c,d,)
print ("f(x)=",y)


