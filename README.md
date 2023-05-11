# Generatore di Test a risposta aperta sulla Funzione Omeografica

## Progetto per docenti di matematica delle scuole secondarie superiori 
Questa libreria permette di generare un test a risposta aperta sulla funzione omeografica 

f(x)=(ax +b)/(cx+d) 

con coefficienti diversi (random interi compresi in un intervallo tra due estremi inclusi) per 
ogni alunno di una data classe. 

La funzione omeografica e' una funzione razionale fratta, che noi trattiamo qui a coefficienti interi, 
che si presta molto bene allo studio di funzione previsto in tutte le scuole secondarie superiori italiane.
Permette di verificare le competenze dell'alunno riguardo ai seguenti obiettivi:
- dominio di una funzione
- intersezioni con gli assi
- simmetrie
- asintoti
- limiti

# Template 
Il testo del test a risposta aperta, uguale per tutti gli studenti, e' il seguente:

1. Trova, se esiste, l'asintoto orizzontale
2. Calcola, se esiste, il valore di `x` corrispondente all'asintoto verticale
3. Calcola le coordinate del centro di simmetria
4. Calcola l'intersezione della funzione con l'asse `x`
5. Calcola l'intersezione della funzione con l'asse `y`

Tutte le domande proposte possono essere risposte a partire dal valore dei coefficienti [a, b, c, d] generati per ogni alunno
Le risposte corrette possono essere valutate calcolando i corrispondenti risultati:
1. y = a/c
2. x = -d/c
3. C = (-d/c, a/c)
4. x = -b/a
5. y = b/d

Tali domande possono essere modificate direttamente dall'utente nel file 'templates\test.md'.

# Cosa serve per usare il pacchetto: dati in input
Per poter usare la libreria e' necessario:
- decidere gli estremi dell'intervallo [e1, e2] a cui appartengono i coefficienti a, b, c, d. Il dominio da inserire deve essere un intervallo di interi, gli estremi verranno considerati inclusi
#TODO: controllare riga sotto
- avere a disposizione un file <classe>.xlsx con una colonna che ha nella prima riga la voce "COGNOME", e nelle righe successive i cognomi degli alunni
- avere a disposizione il percorso assoluto all'interno del dispositivo in uso, o relativo, all'interno della cartella locale, in cui e' salvato il file <classe>.xlsx
#TODO: scrivere nome file
- verificare che tutti i prerequisiti indicati nel file ......... siano soddisfatti (python installato)

# Come usare il pacchetto
Es. [e1, e2] = (-9,9)
    <classe>.xlsx = CLASSE_1A
    percorso file CLASSE_1A = esempio_input\CLASSE_1A

- Scaricare la libreria
- Aprire un terminale e collocarsi nella cartella dove e' stata scaricata la libreria
- Da linea di comando lanciare il modulo 'main' come segue:

`python funzione_omeografica_test\main.py --estremi_dominio=(-9,9) --elenco_alunni=esempio_input\CLASSE_1A
.xlsx`

oppure

`genera_test --estremi_dominio=(-9,9) --elenco_alunni=esempio_input\CLASSE_1A
.xlsx`