##     description="Generatore di Test a risposta aperta sulla Funzione Omeografica.",

# Progetto per docenti di matematica delle scuole secondarie superiori 
Questa libreria permette di generare un test a risposta aperta sulla funzione omeografica 

f(x)=(ax +b)/(cx+d) 

con coefficienti diversi (random interi compresi in un intervallo tra due estremi inclusi) per 
ogni alunno di una data classe. 

La funzione omeografica e' una funzione razionale fratta, che noi trattiamo qui a coefficienti interi, 
che si presta molto bene allo studio di funzione previsto in tutte le scuole secondarie superiori italiane.
Permette di verificare le competenze dell'alunno riguardo lo studio del dominio di una funzione, simmetrie, asintoti, limiti e intersezioni con gli assi
Le domande richieste all'alunno sono le seguenti:

1. Trova, se esiste, l'asintoto orizzontale
2. Calcola, se esiste, il valore di `x` corrispondente all'asintoto verticale
3. Calcola le coordinate del centro di simmetria
4. Calcola l'intersezione della funzione con l'asse `x`
5. Calcola l'intersezione della funzione con l'asse `y`

Tali domande possono essere modificate direttamente dall'utente nel file 'templates\test.md'.

# Cosa serve per usare il pacchetto: dati in input
Per poter usare la libreria e' necessario:
- decidere gli estremi dell'intervallo [e1, e2] a cui appartengono i coefficienti a, b, c, d. Il dominio da inserire deve essere un intervallo di interi, gli estremi verranno considerati inclusi
- avere a disposizione un file <classe>.xlsx con una colonna che ha nella prima riga la voce "COGNOME", e nelle righe successive i cognomi degli alunni
- avere a disposizione il percorso assoluto all'interno del dispositivo in uso, o relativo, all'interno della cartella locale, in cui e' salvato il file <classe>.xlsx
- verificare che tutti i prerequisiti indicati nel file ......... siano soddisfatti (python installato)

# Come usare il pacchetto
Es. [e1, e2] = (-9,9)
    <classe>.xlsx = CLASSE_1A
    percorso file CLASSE_1A = esempio_input\CLASSE_1A

- Scaricare la libreria e collocarsi nella cartella scaricata.
- Aprire un terminale e collocarsi nella cartella scaricata.
- Da linea di comando lanciare il modulo 'main' come segue:

`python funzione_omeografica_test\main.py --estremi_dominio=(-9,9) --elenco_alunni=esempio_input\CLASSE_1A
.xlsx`

oppure

`genera_test --estremi_dominio=(-9,9) --elenco_alunni=esempio_input\CLASSE_1A
.xlsx`