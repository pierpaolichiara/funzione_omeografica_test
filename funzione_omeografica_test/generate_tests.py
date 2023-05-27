""" 
Questo modulo contiene le funzioni necessarie a generare, per ogni cognome di una lista, un testo in cui compaiono la data corrente,
il cognome e dei parametri associati al cognome. Ogni testo viene convertito successivamente in .html per una migliore fruibilita' da parte dell'utente finale.
"""

from sympy import symbols
import os
from datetime import date
from funzione_omeografica_test.generate_abcd_omeo import generate_abcd_omeo
import markdown
#import subprocess
import pandoc
import random as rn

def replace_placeholder(text_line: str, placeholder_id: str, placeholder_value: str):
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


def convert_to_html(md_input_string:str, htm_output_file:str):
    """Questa funzione converte un testo da formato .md a formato .html in un nuovo file"""
    html_string = markdown.markdown(md_input_string, extensions=['markdown.extensions.tables'])
    #utilizziamo il costrutto with open per garantire una sicura chiusura del file quando non e' piu' utilizzato
    with open(htm_output_file, 'w') as f:
        f.write(html_string)

#TODO: togliere o far funzionare conversione in pdf
"""
def convert_html_to_pdf(html_file, pdf_file):
    command = f"pandoc {html_file} -o {pdf_file}"
    subprocess.run(command, shell=True)
"""
def generate_test_from_template(template_content_str: str, output_dir: str, coeffs: list, student_name: str):
    """"
    Questa funzione genera e salva, in una cartella indicata, un testo a partire da un template sotto forma di stringa,
    sostituendo a dei segnaposti i valori indicati in input.

    Il file generato si chiama "test_{student_name}.html" e si trova nella cartella "output" che viene generata quando
    si lancia il main.py.

    Input
    -----
    template_content_str: str
        stringa che contiene il template del testo
    output_dir: str
        indirizzo cartella dove salvare i testi generati dalla funzione
    coeffs: list
        lista di valori di 4 coefficienti interi [a, b, c, d], da inserire al posto degli omologhi placeholders
    student_name: str
        cognome dello studente da inserire al posto dell' omologo placeholder
    """
    #Conosciamo già i placeholder, quindi li listiamo direttamente
    placeholder_student_name = '*NOME_STUDENTE*'
    placeholder_date = '*DATA*'
    placeholder_parameters = ['*VALORE_A*', '*VALORE_B*', '*VALORE_C*', '*VALORE_D*']


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
        for placeholder_param, coef in zip(placeholder_parameters, coeffs):
            maybe_processed_line = replace_placeholder(maybe_processed_line, placeholder_param, f"{coef}")
        test_text_lines.append(maybe_processed_line)

    #crea una cartella 'output' se non la trova che ci serve perche' altrimenti si genera un errore nella
    # generazione dei test individuali
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #crea il percorso completo per un file html nella cartella 'output' denominato 'test_{student_name}.html'
    output_path_html = os.path.join(output_dir, f"test_{student_name}.html")

    #data la lista di stringhe text_test_lines, concatena ogni stringa di testo per avere tutto il testo in una unica
    #stringa perche e'piu' semplice da convertire in un file html rispetto a una lista di stringhe
    md_input_str = ''.join(test_text_lines)
    convert_to_html(md_input_string=md_input_str, htm_output_file=output_path_html)

    #TODO: togliere o far funzionare conversione in pdf
    """
    #convertiamo i testi di verifica anche in pdf per maggiore praticita' di uso e stampa cartacea per l'utente
    output_path_pdf = os.path.join(output_dir, f"test_{student_name}.pdf")
    convert_html_to_pdf(html_file=f"test_{student_name}.html", pdf_file=f"test_{student_name}.pdf")
    """



def generate_tests(template_content_str: str, output_dir: str, student_lists: list, function_domain: tuple):
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
    #TODO: controllare se il link si mette cosi'

    Vedi anche:
    ----------
    random.seed
    """
    e1, e2 = function_domain
    #prima di generare i test per ogni alunno con coefficienti random, inizializziamo un random seed, perche' vogliamo
    # che se l'utente si dovesse trovare, per via di piccole modifiche o altro, a lanciare piu' volte il programma,
    # una volta selezionata la lista di studenti, a ogni alunno venga assegnata sempre la stessa quaterna.
    rn.seed(10)
    for student_name in student_lists:
        abcd_list = generate_abcd_omeo(e1, e2)
        generate_test_from_template(template_content_str=template_content_str, output_dir=output_dir, coeffs=abcd_list, student_name=student_name)

    #  html_file =generate_test_from_template(template_content_str=template_content_str, output_dir=output_dir, coeffs=abcd_list, student_name=student_name)


if __name__ == "__main__":
    main()
