# Generatore di Test a risposta aperta sulla Funzione Omeografica
## Progetto per docenti di matematica delle scuole secondarie superiori

### Introduzione
Questa libreria permette di generare un test di verifica a risposta aperta sulla Funzione Omeografica (in seguito FO) 

f(x)=(ax +b)/(cx+d) 

con coefficienti [a,b,c,d] (random interi compresi in un intervallo tra due estremi inclusi) che variano per ogni alunno 
di una data classe. 

La FO e' una funzione razionale fratta, trattata qui a coefficienti interi, che si presta molto bene allo studio di 
funzione, previsto dalle Indicazioni Nazionali in tutte le scuole secondarie superiori italiane.
Permette di verificare le competenze dell'alunno nell'affrontare i seguenti argomenti:
- dominio di una funzione
- intersezioni con gli assi
- simmetrie
- asintoti
- limiti

### Template 
Il testo del test di verifica a risposta aperta, uguale per tutti gli studenti, e' il seguente:

1. Trova, se esiste, l'asintoto orizzontale
2. Calcola, se esiste, il valore di `x` corrispondente all'asintoto verticale
3. Calcola le coordinate del centro di simmetria
4. Calcola l'intersezione della funzione con l'asse `x`
5. Calcola l'intersezione della funzione con l'asse `y`

Tutte le domande proposte possono essere risposte a partire dal valore dei coefficienti [a, b, c, d] generati per ogni alunno.
Le risposte corrette possono essere valutate calcolando i corrispondenti risultati:
1. y = a/c
2. x = -d/c
3. C = (-d/c, a/c)
4. x = -b/a
5. y = b/d

Le domande proposte possono essere modificate direttamente dall'utente nel file 'templates\test.md'.

### Cosa serve per usare la libreria: 
#### Dati in input
Per utilizzare la libreria e' necessario:
1. decidere gli estremi dell'intervallo [e1, e2] a cui appartengono i coefficienti a, b, c, d. Il dominio da inserire deve 
essere un intervallo di interi, gli estremi verranno considerati inclusi
2. avere a disposizione un file <classe>.xlsx o <classe>.xls con una colonna che ha nella prima riga la voce "COGNOME" 
scritta in maiuscolo, e nelle righe successive della stessa colonna i cognomi degli alunni della classe per cui generare
e stampare i test
3. avere a disposizione il percorso assoluto, all'interno del dispositivo in uso, in cui e' salvato il file <classe>.xlsx 
o <classe>.xls
4. Facoltativo: avere a disposizione il percorso assoluto, all'interno del dispositivo in uso, in cui salvare i test di 
verifica generati in output per la classe scelta

#### Prerequisiti di configurazione
- Avere una Common Line Interface (CLI) nel dispositivo in uso.
- Avere Python installato nel dispositivo in uso. La libreria e' stata testata per la versione di Python 3.9.13. 

Librerie aggiuntive necessarie (che si possono leggere nei file [requirements_base.txt](https://github.com/pierpaolichiara/funzione_omeografica_test/blob/main/requirements-base.txt) e in [requirements-test.txt](https://github.com/pierpaolichiara/funzione_omeografica_test/blob/main/requirements-test.txt) vengono installate automaticamente se necessario una volta lanciato il file principale.

#### Installazione e utilizzo
Per poter usare la libreria e' necessario:

5. clonare il repository https://github.com/pierpaolichiara/funzione_omeografica_test da CLI con il seguente comando:

`git clone https://github.com/pierpaolichiara/funzione_omeografica_test`

6. aprire la cartella 'funzione_omeografica_test' che e' stata scaricata con il comando 

`cd funzione_omeografica_test`

7. installare la libreria 

`pip install .`

8. lanciare il file main.py come segue

`python funzione_omeografica_test\main.py --estremi_dominio=(e1,e2) --elenco_alunni=<classe.xlsx>`
   
oppure

`genera_test --estremi_dominio=(e1,e2) --elenco_alunni=<classe.xlsx>`


dove sostituire 
- a `e1` ed `e2` gli estremi scelti nel punto 1 
- a `<classe.xlsx>` il percorso assoluto del file excel (o relativo se nella cartella corrente) con l'elenco degli alunni del punto 2
- (facoltativo) si puo' specificare, volendo, la cartella in cui si vuole vengano salvati i test generati. Per farlo bisogna 
aggiungere al comando scelto nel punto 8 quanto segue:

` --cartella_output=<percorso_cartella_output>`

e sostituendo a `<percorso_cartella_output>` il percorso assoluto della cartella di output desiderata individuato 
nel punto 5.

### Esempio
Consideriamo questi dati come esempio di utilizzo della libreria:

`(e1, e2)` = `(-9,9)`

<classe.xlsx> = `CLASSE_1A.xlsx`

percorso file CLASSE_1A = esempio_input\CLASSE_1A

![img_1.png](img_1.png)

Per stampare in .html i test a risposta aperta sulla Funzione Omeografica con i dati dell'esempio come input: 
- Scaricare la libreria
- Aprire un terminale e collocarsi nella cartella dove e' stata scaricata la libreria
- Da linea di comando lanciare il modulo 'main' come segue:

`python funzione_omeografica_test\main.py --estremi_dominio=(-9,9) --elenco_alunni=esempio_input\CLASSE_1A
.xlsx`

oppure

`genera_test --estremi_dominio=(-9,9) --elenco_alunni=esempio_input\CLASSE_1A
.xlsx`

- i test stampati in .html sono disponibili nella cartella 'funzione_omeografica_test/output', denominati con il cognome dell'alunno nel seguente modo:
`test_<COGNOME>.html`,
ad esempio test_ALFA.html, test_BETA.html... 
Riportiamo un esempio di
test di verifica stampato:
![img_2.png](img_2.png)

## Struttura della libreria funzione_omeografica_test
La libreria

