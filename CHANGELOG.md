## SCREENSHOT PROGETTO 2023 05 04

#Unrealized

- cambiare random in random seed
- spostare i suggerimenti di test in file appositi
- collegamento a random choice in genera ceoff

- modificare random.choice per seq int con random.uniform per float? solo che poi se gli estremi 
	non sono ordinati vanno cambiati i test e la fuznione perche' funzionerebbe cmq



#Added
- controllo delta su coefficienti

#Removed
- dominio_rel con output solo list
- eliminare file genera coeff abcd 0 e 2
- eliminare file fz_dominio
#Changed
eliminate funzioni obsolete
usare 
- dominio_rel.py
- fz_genera_coeff_abcd2.py #FIX CASO DELTA=0 #DONE
- def genera dominio da'un output DI TROPPO (nONE) nel caso e1>=e2: tolto return 
finale pero'il return non avra'tipo predefinito, o list o str -> test type

#Deprecated
dominio_rel.py
fz_genera_coeff_abcd0.py
fz_genera_coeff_abcd2.py