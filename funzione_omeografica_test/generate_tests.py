""" 
Questo modulo contiene le funzioni necessarie a generare, per ogni cognome di una lista, un testo in cui compaiono la data corrente,
un cognome e dei parametri associati al cognome. Ogni testo viene convertito successivamente in .html per una migliore
fruibilita' da parte dell'utente finale.
"""

from sympy import symbols
import os
from datetime import date
from funzione_omeografica_test.generate_abcd_omeo import generate_abcd_omeo
import markdown
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
    str: e'la stringa in input con eventuale segnaposto sostituito col suo valore
    """
    if placeholder_id in text_line:
        new_line = text_line.replace(placeholder_id, placeholder_value)
        return new_line
    else:
        return text_line


def generate_param_strings(coeffs):
    """
    # TODO
    """
    a, b, c, d = coeffs
    a_sign = "-" if a < 0 else ""
    a_str = "" if a == 0 else f"{a_sign} x" if abs(a) == 1 else f"{a_sign}{abs(a)} x"
    b_sign = "-" if b < 0 else "" if (b == 0 or a_str == "") else "+"
    b_str = f"{b_sign} {abs(b)}" if b != 0 else f""
    c_sign = "-" if c < 0 else ""
    c_str = f"{c_sign}" if abs(c) == 1 else f"{c_sign}{abs(c)}"
    d_sign = "-" if d < 0 else "" if d == 0 else "+"
    d_str = f"{d_sign} {abs(d)}" if d != 0 else f""
    return a_str, b_str, c_str, d_str

def generate_test_from_template(template_content_str: str, coeffs: list, student_name: str):
    """
    Questa funzione genera e salva, in una cartella indicata, un testo .html a partire da un template sotto forma di stringa,
    sostituendo a dei segnaposti i valori indicati in input.

    Il file generato si chiama "test_{student_name}.html" e si trova nella cartella "output" che viene generata quando
    si lancia il main.py.

    Input
    -----
    template_content_str: str
        stringa che contiene il template del testo
    coeffs: list
        lista di valori di 4 coefficienti interi [a, b, c, d], da inserire al posto degli omologhi placeholders
    student_name: str
        cognome dello studente da inserire al posto dell' omologo placeholder
    """
    #Conosciamo già i placeholder, quindi li listiamo direttamente
    placeholder_student_name = '*NOME_STUDENTE*'
    placeholder_date = '*DATA*'
    placeholder_parameters = ['*VALORE_AX*', '*VALORE_B*', '*VALORE_C*', '*VALORE_D*']

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

        params_strings = generate_param_strings(coeffs)
        for placeholder_param, param_str in zip(placeholder_parameters, params_strings):
            maybe_processed_line = replace_placeholder(maybe_processed_line, placeholder_param, param_str)

        test_text_lines.append(maybe_processed_line)

    #data la lista di stringhe text_test_lines, concatena ogni stringa di testo per avere tutto il testo in una unica
    md_input_str = ''.join(test_text_lines)
    html_string = markdown.markdown(md_input_str, extensions=['markdown.extensions.tables'])
    return html_string


def generate_tests(template_content_str: str, output_dir: str, student_lists: list, function_domain: tuple, class_id: str):
    """
    Questa funzione genera, con un ciclo, un insieme di testi di verifica, uno diverso per studente di una lista, dove
    a cambiare sono il cognome dello studente e i coefficienti che variano all'interno di un dominio indicato.

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


    Vedi anche:
    ----------
    random.seed(): https://docs.python.org/3/library/random.html?highlight=random%20seed#random.seed
    """
    e1, e2 = function_domain
    #prima di generare i test per ogni alunno con coefficienti random, inizializziamo un random seed, perche' vogliamo
    # che se l'utente si dovesse trovare, per via di piccole modifiche o altro, a lanciare piu' volte il programma,
    # una volta selezionata la lista di studenti, a ogni alunno venga assegnata sempre la stessa quaterna.

    #FIXME: FAR INSERIRE ALL'UTENTE UN NUMERO PER RANDOM SEED-> lo prendo dal main
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
        student_test_html = generate_test_from_template(template_content_str=template_content_str, coeffs=abcd_list, student_name=student_name)

        #crea il percorso completo per un file html nella cartella 'output' denominato 'test_{student_name}.html'
        output_path_html = os.path.join(output_dir, f"test_{student_name}.html")
        with open(output_path_html, 'w') as f:
            f.write(student_test_html)
