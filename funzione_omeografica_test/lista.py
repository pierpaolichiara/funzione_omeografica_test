# -*- coding: utf-8 -*-
"""

"""

import pandas as pd
import os


def parse_student_list(student_list_path: str):
    if not os.path.exists(student_list_path):
        raise IOError(f"Il file {student_list_path} non esiste.")

    if not os.path.basename(student_list_path).endswith(('xls', 'xlsx')):
        raise TypeError("La lista degli studenti deve essere in formato excel")


    dataframe=pd.read_excel(student_list_path, index_col=0)
    # print(dataframe)
    #print(dataframe["COGNOME"])

    names = dataframe["COGNOME"].values.tolist()
    return names

def boh(dataframe):
    zeta={}
    for name in dataframe["COGNOME"]:
        #print(name)
        zeta[name]=fz_genera_coeff_abcd.assegna_abcd()
    print(zeta)

    dati=pd.DataFrame.from_dict(zeta).transpose()
    dati.columns=["a","b","c","d"]
    dati.to_excel("DATI.xlsx")
    print(dati['c']['BETA'])

#STAMPARE FOGLI PDF 
#-UNO PER OGNI ALUNNO CON SUO FZ, E DOMANDE
#-PER OGNI INSEGNANTE UN FOGLIO CON DOMANDE, COMPITO DI OGNI ALUNNO, PLOT E SOLUZIONI