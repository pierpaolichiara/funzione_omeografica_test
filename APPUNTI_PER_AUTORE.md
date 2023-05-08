## SCREENSHOT PROGETTO 2023 05 05

#Unrealized
- finire documentazione g_omeo.py enerate_abcd 
- from generate_abcd_omeo.py import parse_function_domain: togliere le virgolette ??? inserire direttamente e1 ed e2?
- fare file con approfondimenti e scelte separato dal readme?
- sistemare gli import nel posto giusto
- sistemare le descrizioni delle funzioni
- inserire random seed--> se lo inserisco prima dei 4 random.choice, per ogni studente avro' lo stesso vettore!!!
	va inizializzato nella funzione di generazione vettori per la classe
- spostare i suggerimenti di test in file appositi
- collegamento a random choice in genera ceoff

- modificare random.choice per seq int con random.uniform per float? solo che poi se gli estremi 
	non sono ordinati vanno cambiati i test e la fuznione perche' funzionerebbe comunque
-motivare scelta del metodo random in random: random.choice, invece di choices, randint, randrange...
                                  non in numpy.random....test?
- aggiungere idea di funzioni separate per essere riutilizzabili per altre evenienze

#Added
-creata assegna_abcd.py, fz da usare con dominio_int.py per generare i 4 coeff: con queste due fz genero dominio che posso testare ed eventualmente 
 eliminare un elemento, e assegnare i coefficienti a partire da un unico dominio, con ctrl sulle 2 condizioni di esistenza
-creata fz_dominio_coeff.py, unica fz per creazione vettore coeff a partire da dominio con estremi indicati in input(non posso pero'testare il dominio)- controllo delta su coefficienti
- controllo su c
-controllo su delta

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
dominio_coeff.py
fz_genera_coeff_abcd0.py
fz_genera_coeff_abcd2.py
fz_genera_coeff_abcd.py

#NOTE E DUBBI
1-tenuta fz per generare dominio separata perche' utilizzabile per altre cose e per variare tipo di dati, magari float
2-la funzione omeografica ha 2 C.N. per essere propria. si potrebbe EVITARE DUE DOMINI IN INGRESSO, inserire cn1 c!=0 
 nella fz assegna_abcd con un altro while
	c=0
	while c==0:			#verifica C.N.1
		c=radom.choice(dominio1)
	delta=0
   	while delta==0:                 #verifica C.N.2
        	a=random.choice(dominio1)        
        	b=random.choice(dominio1)
        	d=random.choice(dominio1)
        	delta=a*d-c*b

