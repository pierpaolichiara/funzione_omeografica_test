# -*- coding: utf-8 -*-
"""
Questo modulo serve a estrarre i cognomi degli alunni di una classe da un file excel e generare una lista con i cognomi,
da utilizzare nel modulo 'main.py' come variabile della funzione 'generate_tests'.
"""

import pandas as pd
import os


def parse_student_list(student_list_path: str)->list:
    """
    Dato un file excel, la funzione legge il file excel e converte i contenuti della colonna intitolata "COGNOME" in
    una lista.

    Del file excel viene fornito in input il percorso dispositivo in uso: il file deve contenere la scritta "COGNOME"
    nella prima cella di una sua colonna,diversa dalla prima.

    Input
    -----
    student_list_path: str
        percorso assoluto del file excel

    Output
    ------
    list: [ALFA, BETA, CHARLIE...]
        lista di stringhe, corrispondenti ai cognomi inseriti nel file excel
    """
    if not os.path.exists(student_list_path):
        raise NameError(f"Il file {student_list_path} non esiste.")
    #todo: funziona ma non sostituisce il percorso dentro le graffe
    if not os.path.basename(student_list_path).endswith(('xls', 'xlsx')):
        raise TypeError("La lista degli studenti deve essere in formato excel")

    # legge la colonna "COGNOME" del file e genera la lista dei cognomi
    dataframe = pd.read_excel(student_list_path, index_col=0)

    if dataframe.empty:
        print("Il file excel indicato contiene una lista di cognomi vuota")
    #non continuiamo con un else perche' altrimenti, quando si fa girare il main con un excel vuoto non compare la
    #scritta del print sopra ma errori in altre funzioni che hanno come argomento il return di questa funzione
    if not 'COGNOME' in dataframe['COGNOME'].values:
        print("La lista dei cognomi non e' accessibile dalla seconda colonna del file excel indicato. \n"
              "Controlla che la seconda colonna del file excel abbia la scritta COGNOME nella cella della prima riga")
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
#fixme: TEST: provare parse_student_list con file xls di prova
#a=parse_student_list('C:/Users/Matteo/funzione_omeografica_test/test/excel_di_prova/PRIMACOL.xlsx')
#print(a)
#KeyError: 'COGNOME'

#a=parse_student_list('C:/Users/Matteo/funzione_omeografica_test/test/excel_di_prova/SOLOTIT.xlsx')
#print(a)
#da' lista []

#a=parse_student_list('C:/Users/Matteo/funzione_omeografica_test/test/excel_di_prova/VUOTO.xlsx')
#print(a)
#    raise KeyError(key) from err
#KeyError: 'COGNOME'




