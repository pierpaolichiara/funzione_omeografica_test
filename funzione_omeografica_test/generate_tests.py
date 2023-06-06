""" 
Questo modulo contiene le funzioni necessarie a generare, per ogni cognome di una lista, un testo in cui compaiono la data corrente,
un cognome e dei parametri associati al cognome. Ogni testo viene convertito successivamente in .html per una migliore
fruibilita' da parte dell'utente finale.
"""

import os
from datetime import date
from funzione_omeografica_test.generate_abcd_omeo import generate_abcd_omeo
import markdown
from sympy import Symbol
#from sympy import Poly
import random as rn
from funzione_omeografica_test.empty_folder import empty_folder

def replace_placeholder(text_line: str, placeholder_id: str, placeholder_value: str)-> str:
    """
    Questa funzione legge il template e sostituisce i segnaposti (placeholder <>) con i valori opportuni stringa per stringa,
    riscrivendo il testo del file riga per riga

    Input
    ------
    text_line: str
        stringa di testo
    placeholder_id: str
        nome del segnaposto eventualemente presente nella stringa
    placeholder_value: str
        valore del segnaposto da sostituire al posto del placeholder_id

    Output
    ------
    str: stringa in input con eventuale segnaposto sostituito col suo valore
    """
    if placeholder_id in text_line:
        new_line = text_line.replace(placeholder_id, placeholder_value)
        return new_line
    else:
        return text_line

def num_den(coeffs: list)->tuple:
    """
    Questa funzione esegue il calcolo simbolico sostituendo 4 coefficienti [a,b,c,d] nelle espressioni algebriche
    ax+b e cx+d, e converte i due risultati in stringhe di una tupla

    Input
    -----
    coeffs: list
        lista di 4 interi

    Output
    ------
    (num_str, den_str): tuple
        (ax+b, cx+d) calcolati e convertiti in stringhe
    """
    x = Symbol('x')
    a, b, c, d = coeffs
    #il programma calcola i due oggetti seguenti e li memorizza con l'ordine dei monomi che da' una migliore resa estetica
    num_x = a * x + b
    den_x = c * x + d
    # Creazione dell'oggetto polinomiale per manipolazione successiva
     #  num = Poly(num, x)
     #   den = Poly(den, x)
    # Ordiniamo i monomi di num e den per grado decrescente, per avere una formula
    # finale nel test piu' pulita e uguale per tutti gli studenti nella forma (ax+b)/(cx+d)
     # num_x = num.as_ordered_terms()
    # den_x = den.as_ordered_terms()
    num_str = str(num_x).replace('*', '')
    den_str = str(den_x).replace('*', '')
    return (num_str, den_str)


def generate_test_from_template(template_content_str: str, coeffs: list, student_name: str, class_id: str):
    """
    Questa funzione genera un testo .html a partire da un template sotto forma di stringa,
    sostituendo a dei segnaposti i valori indicati in input.

    Input
    -----
    template_content_str: str
        stringa che contiene il template del testo
    coeffs: list
        lista di valori di 4 coefficienti interi [a, b, c, d], da inserire al posto degli omologhi placeholders
    student_name: str
        cognome dello studente da inserire al posto dell' omologo placeholder
    class_id: str
        codice identificativo della lista sudenti a cui appartiene lo student_name, inserito in input

    Output
    ------
    html_string: str
        stringa contenente il testo di verifica di un alunno composto a partire dagli input
    """
    #Conosciamo già i placeholder, quindi li listiamo direttamente
    placeholder_class_id = '*ID_CLASSE*'
    placeholder_student_name = '*NOME_STUDENTE*'
    placeholder_date = '*DATA*'
    placeholder_fraction = ['*NUMERATOR*', '*DENOMINATOR*']

    #Dividiamo la stringa contenente il testo del template in sottostringhe corrispondenti alle righe del template,
    #in corrispondenza del carattere di 'a-capo', perche' nel ciclo for piu' sotto ci servira' il testo del template
    #passato come lista di stringhe per sostituire i placeholder, per poi riunire le stringhe in un unico file md da convertire in html.
    #Abbiamo provato a fare tutto cio' inizialmente sostituendo i placeholder in un file .md ma il codice generava un errore.

    #Ri-aggiungiamo il carattere 'a-capo' ad ogni riga. Abbiamo ora una lista di stringhe chiamata 'template_text' in cui a
    #ogni stringa corrisponde una riga del template
    template_text = [l + "\n" for l in template_content_str.split("\n")]

    today = date.today()
    # dd/mm/YY
    today_date_str = today.strftime("%d/%m/%Y")

    #inizializzazione del testo della verifica come stringa vuota che riempiremo nel ciclo sottostante
    test_text_lines = []

    for template_line in template_text:
        #per ogni riga di testo del template vengono sostituiti ad eventuali segnaposto (placeholder) definiti sopra
        #i loro rispettivi valori e la riga di testo viene riportata in una stringa in cui troveremo come risultato il
        #testo finale della verifica
        maybe_processed_line = replace_placeholder(template_line, placeholder_student_name, student_name)
        maybe_processed_line = replace_placeholder(maybe_processed_line, placeholder_date, today_date_str)
        maybe_processed_line = replace_placeholder(maybe_processed_line, placeholder_class_id, class_id)
        params_strings = num_den(coeffs)
        # sostituire i coefficienti a, b, c, d (sotto: coeffs) direttamente all'interno della formula attraverso i relativi
        # placeholder porterebbe a inconvenienti di segni all'interno della formula: es, a=-1, b=-2, c=-3, d=+4 produrrebbe
        #               f(x)=(-1*a+-2)/(-3*c+4),
        # pertanto si rende necessario l'uso della funzione num_den: calcoliamo numeratore e denominatore della funzione
        # omeografica utilizzando le funzionalita' di Sympy, per poi convertirli in stringa in modo da poter togliere il simbolo * della moltiplicazione.
        # per un migliore rendering estetico nel testo finale

        for placeholder_frac, param_str in zip(placeholder_fraction, params_strings):
            maybe_processed_line = replace_placeholder(maybe_processed_line, placeholder_frac, param_str)

        test_text_lines.append(maybe_processed_line)

    #data la lista di stringhe text_test_lines, concatena ogni stringa di testo per avere tutto il testo in una unica
    md_input_str = ''.join(test_text_lines)
    html_string = markdown.markdown(md_input_str, extensions=['markdown.extensions.tables'])
    return html_string


def generate_tests(template_content_str: str, output_dir: str, student_lists: list, function_domain: tuple, class_id: str):
    """
    Questa funzione genera, con un ciclo, un insieme di test di verifica associato a un codice identificativo, un test
    diverso per ogni studente di una lista indicata, dove a cambiare sono il cognome dello studente e i coefficienti che
    variano all'interno di un dominio indicato.
    Ogni insieme di test generati viene salvato nella cartella "output" generata quando si lancia il main.py.
    Il nome di ogni file e' "test_{class_id}_{student_name}.html"

    Input
    -----
    template_content_str: str
        stringa con il template del testo, da passare alla funzione `generate_test_from_template()`
    output_dir: str
        cartella dove vengono salvati i test generati in .html, da passare alla funzione `generate_test_from_template()`
    student_lists: list
        lista dei cognomi degli studenti su cui iterare la generazione dei test
    function_domain: tuple
        intervallo di interi, estremi compresi, in cui vengono scelti i coefficienti della lista di interi associata a
        ogni cognome con il modulo [generate_abcd_omeo.py](https://github.com/pierpaolichiara/funzione_omeografica_test)
    class_id: str
        codice scelto dall'utente in fase di input identificativo dei test generati per il gruppo di alunni spercificato
        nella student_list

    Vedi anche:
    ----------
    random.seed(): https://docs.python.org/3/library/random.html?highlight=random%20seed#random.seed
    """
    e1, e2 = function_domain
    #prima di generare i test per ogni alunno con coefficienti random, inizializziamo un random seed, scelto dall'utente in input,
    # perche' vogliamo che se l'utente si dovesse trovare, per via di piccole modifiche o altro, a lanciare piu' volte il programma,
    # una volta selezionata la lista di studenti, a ogni alunno venga assegnata sempre la stessa quaterna.

    rn.seed(class_id)

    #crea una cartella 'output', se al percorso in input non corrisponde nessuna cartella, che ci serve perche' altrimenti
    # si genera un errore nella generazione dei test individuali
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    else:
        #svuota la cartella di output se gia' esistente
        empty_folder(output_dir)

    for student_name in student_lists:
        abcd_list = generate_abcd_omeo(e1, e2)
        student_test_html = generate_test_from_template(template_content_str=template_content_str, coeffs=abcd_list, student_name=student_name, class_id=class_id)
        #crea il percorso completo per un file html nella cartella 'output' denominato 'test_{class_id}_{student_name}.html'
        #e ci salva la stringa con il test dello studente
        output_path_html = os.path.join(output_dir, f"test_{class_id}_{student_name}.html")
        with open(output_path_html, 'w') as f:
            f.write(student_test_html)
