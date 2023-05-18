# -*- coding: utf-8 -*-
"""
#TODO: documentazione
"""

import pandas as pd
import os


def parse_student_list(student_list_path: str)->list:
    if not os.path.exists(student_list_path):
        raise IOError(f"Il file {student_list_path} non esiste.")

    if not os.path.basename(student_list_path).endswith(('xls', 'xlsx')):
        raise TypeError("La lista degli studenti deve essere in formato excel")

    dataframe = pd.read_excel(student_list_path, index_col=0)
#legge la colonna cognome del file e genera la lista dei cognomi
    names = dataframe["COGNOME"].values.tolist()
    return names
