""" 
Questo modulo contiene le funzioni necessarie a generare, per ogni cognome di una lista, un testo in cui compaiono la data corrente,
il cognome e dei parametri associati al cognome. Ogni testo viene convertito successivamente in .html per una migliore fruibilita' da parte dell'utente finale.
"""

from sympy import symbols
import os
from datetime import date
from funzione_omeografica_test.generate_abcd_omeo import generate_abcd_omeo
import markdown

def replace_placeholder(text_line: str, placeholder_id: str, placeholder_value: str):
    """
    Questa funzione legge il template e sostituisce i segnaposti (placeholder <>) con i valori opportuni stringa per stringa,
    riscrivendo il testo del file riga per riga
    """
    if placeholder_id in text_line:
        new_line = text_line.replace(placeholder_id, placeholder_value)
        return new_line
    else:
        return text_line


def convert_to_html(md_input_string:str, htm_output_file:str):
    """Questa funzione prende una stringa di testo in formato md e la scrive in un file html"""
    html_string = markdown.markdown(md_input_string, extensions=['markdown.extensions.tables'])
    with open(htm_output_file, 'w') as f:
        f.write(html_string)


def generate_test_from_template(template_content_str:str, output_dir:str, coeffs:list, student_name:str):
    """"
    Questa funzione genera e salva, in una cartella indicata, un testo a partire da un template sotto forma di stringa,
    sostituendo a dei segnaposti i valori indicati in input
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

    #inizializzazione del testo della verifica come stringa vuota che ci servira' da riempire nel ciclo sottostante
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
    output_path = os.path.join(output_dir, f"test_{student_name}.html")

    #data la lista di stringhe text_test_lines, concatena ogni stringa di testo per avere tutto il testo in una unica
    #stringa perche e'piu' semplice da convertire in un file html rispetto a una lista di stringhe
    md_input_str = ''.join(test_text_lines)
    convert_to_html(md_input_string=md_input_str, htm_output_file=output_path)


def generate_tests(template_content_str: str, output_dir: str, student_lists: list, function_domain: tuple):
    """
    Questa funzione genera, con un ciclo, un insieme di testi di verifica, uno diverso per ogni cognome di studente, dove
    a cambiare sono il cognome dello studente e i coefficienti che variano all'interno di un dominio indicato.
    """
    e1, e2 = function_domain
    for student_name in student_lists:
        abcd_list = generate_abcd_omeo(e1, e2)
        generate_test_from_template(template_content_str=template_content_str, output_dir=output_dir, coeffs=abcd_list, student_name=student_name)


if __name__ == "__main__":
    main()
