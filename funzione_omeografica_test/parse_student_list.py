# -*- coding: utf-8 -*-
"""
Questo modulo serve a estrarre i cognomi degli alunni di una classe da un file excel e generare una lista con i cognomi,
da utilizzare nel modulo 'main.py' come variabile della funzione 'generate_tests'.
"""

import pandas as pd
import os


def parse_student_list(student_list_path: str)-> list:
    """
    Dato un file excel, la funzione legge il file excel e converte i contenuti della colonna intitolata "COGNOME" in
    una lista.

    Del file excel viene fornito in input il percorso nel dispositivo in uso: il file deve contenere la scritta "COGNOME"
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

    if not os.path.basename(student_list_path).endswith(('xls', 'xlsx')):
        raise TypeError("La lista degli studenti deve essere in formato excel")

    # legge la colonna "COGNOME" del file e genera la lista dei cognomi
    dataframe = pd.read_excel(student_list_path, index_col=0)

    if dataframe.empty:
        raise TypeError("\n\nERRORE:Il file excel indicato e' vuoto o la seconda colonna (colonna B) del file e'vuota: "
                        "non riesco ad estrarre nessuna lista di cognomi.\n "
                        "Rileggi le indicazioni sulla formattazione dei file di input qui: https://github.com/pierpaolichiara/funzione_omeografica_test/blob/main/README.md \n")
    #non continuiamo con un else perche' altrimenti, quando si fa girare il main con un excel vuoto non compare la
    #scritta del print sopra ma errori in altre funzioni che hanno come argomento il return di questa funzione

    elif not 'COGNOME' in dataframe.columns:
            raise KeyError("\n\nERRORE: La lista dei cognomi non e' accessibile dalla seconda colonna, ne' dalle successive,  del file excel indicato. "
                        "Controlla che il file excel abbia la scritta COGNOME nella cella B1, cioe' prima riga e seconda colonna.\n\n")
    else:
    #converte il contenuto della colonna "COGNOME" in una lista
        names = dataframe["COGNOME"].tolist()
        return names
