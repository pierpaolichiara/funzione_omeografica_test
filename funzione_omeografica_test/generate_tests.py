""" 
Questa funzione genera una funzione omeografica a partire da 4 coefficienti
    
Parametri in input
------------------
a, b, c, d: coefficienti della funzione omeografica

Output
------
f(x)=(a*x+b)/(c*x+d)
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
    #Conosciamo già i placeholder, quindi li listiamo direttamente
    placeholder_student_name = '*NOME_STUDENTE*'
    placeholder_date = '*DATA*'
    placeholder_parameters = ['*VALORE_A*', '*VALORE_B*', '*VALORE_C*', '*VALORE_D*']

    #divide la stringa con il testo del template in righe in corrispondenza del carattere di 'a-capo'.
    #Ri-aggiunge il carattere 'a-capo' ad ogni riga
    template_text = [l + "\n" for l in template_content_str.split("\n")]

    today = date.today()
    # dd/mm/YY
    today_date_str = today.strftime("%d/%m/%Y")

    #inizializzazione del testo della verifica come stringa vuota che ci servira' da riempire nel ciclo sottostante
    test_text_lines = []

    for template_line in template_text:
        #per ogni riga di testo del template vengono sostituiti ad eventuali segnaposto (placeholder) definiti sopra
        #i loro rispettivi valori e la riga di testo viene riportata nella stringa in cui troveremo come risultato il
        #testo finale della verifica
        maybe_processed_line = replace_placeholder(template_line, placeholder_student_name, student_name)
        maybe_processed_line = replace_placeholder(maybe_processed_line, placeholder_date, today_date_str)
        for placeholder_param, coef in zip(placeholder_parameters, coeffs):
            maybe_processed_line = replace_placeholder(maybe_processed_line, placeholder_param, f"{coef}")
        test_text_lines.append(maybe_processed_line)

    #crea una cartella 'output' se non la trova
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #crea un file html nella cartella 'output' denominato 'test_{student_name}.html'
    output_path = os.path.join(output_dir, f"test_{student_name}.html")

    #concateniamo le righe di testo per avere tutto il testo in una unica stringa da convertire in un file html
    md_input_str = ''.join(test_text_lines)
    convert_to_html(md_input_str, output_path)


def generate_tests(template_content_str: str, output_dir: str, student_lists: list, function_domain: tuple):
    e1, e2 = function_domain
    for student_name in student_lists:
        abcd_list = generate_abcd_omeo(e1, e2)
        generate_test_from_template(template_content_str=template_content_str, output_dir=output_dir, coeffs=abcd_list, student_name=student_name)


if __name__ == "__main__":
    main()
