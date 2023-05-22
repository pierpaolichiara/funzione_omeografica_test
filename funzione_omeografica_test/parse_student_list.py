# -*- coding: utf-8 -*-
"""
Questo modulo serve a estrarre i cognomi degli alunni di una classe da un file excel e generare una lista con i cognomi,
da utilizzare nel modulo main come variabile della funzione 'generate_tests'.
"""

import pandas as pd
import os


def parse_student_list(student_list_path: str)->list:
    """
    Dato un file excel esistente nel dispositivo in uso, che contenga la scritta "COGNOME" nella prima cella di una sua colonna,
    la funzione legge il file excel e converte i contenuti della colonna intitolata "COGNOME" in una lista
    """
    if not os.path.exists(student_list_path):
#       raise IOError(f"Il file {student_list_path} non esiste.")
        raise NameError(f"Il file {student_list_path} non esiste.")
#FIXME: viene dato un errore NameError, diverso da IOError indicato, e la frase in italiano non compare
    if not os.path.basename(student_list_path).endswith(('xls', 'xlsx')):
        raise TypeError("La lista degli studenti deve essere in formato excel")

    dataframe = pd.read_excel(student_list_path, index_col=0)
#legge la colonna cognome del file e genera la lista dei cognomi
    names = dataframe["COGNOME"].tolist()
    return names

#controesempio al fixme
#b=ont.xls
#print(b)
#a=parse_student_list(b)
#print(a)

#controesempio caso non xls che funziona
c= os.path.abspath(__file__)
print(c)
#a=parse_student_list(c)
#print(a)
#fixme: provare parse_student_list con file xls di prova
#a=parse_student_list('C:/Users/Matteo/funzione_omeografica_test/esempio_input/PRIMACOL.xlsx')
#print(a)
#KeyError: 'COGNOME'

#a=parse_student_list('C:/Users/Matteo/funzione_omeografica_test/esempio_input/SOLOTIT.xlsx')
#print(a)
#da' lista []

#a=parse_student_list('C:/Users/Matteo/funzione_omeografica_test/esempio_input/VUOTO.xlsx')
#print(a)
#    raise KeyError(key) from err
#KeyError: 'COGNOME'




