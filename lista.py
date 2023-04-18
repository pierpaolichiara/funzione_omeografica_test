# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:16:26 2023

@author: Matteo
"""

import pandas as pd
import fz_genera_coeff_abcd0

dataframe=pd.read_excel("CLASSE_1A.xlsx", index_col=0)
print(dataframe)
#print(dataframe["COGNOME"])

zeta={}
for name in dataframe["COGNOME"]:
    #print(name)
    zeta[name]=fz_genera_coeff_abcd0.assegna_abcd()
print(zeta)

dati=pd.DataFrame.from_dict(zeta).transpose()
dati.columns=["a","b","c","d"]
dati.to_excel("DATI.xlsx")
print(dati['c']['BETA'])