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
from funzione_omeografica_test.assegna_abcd_omeo import generate_abcd_omeo
import markdown

def genera_fz_omeografica(a, b, c, d):
    x = symbols("x")
    f_x = (a * x + b) / (c * x + d)
    return f_x


def replace_placeholder(text_line: str, placeholder_id: str, placeholder_value: str):
    if placeholder_id in text_line:
        new_line = text_line.replace(placeholder_id, placeholder_value)
        return new_line
    else:
        return text_line


def convert_to_html(md_input_string:str, htm_output_file:str):
    html_string = markdown.markdown(md_input_string, extensions=['markdown.extensions.tables'])
    with open(htm_output_file, 'w') as f:
        f.write(html_string)


def generate_test_from_template(template_path, output_dir, coeffs, student_name):
    if not os.path.exists(template_path):
        raise IOError(f"Il template {template_path} non esiste.")

    if not os.path.basename(template_path).endswith('md'):
        raise TypeError("Il template deve essere in formato .md")

    # Conosciamo già i placeholder, quindi li listiamo direttamente
    placeholder_student_name = '*NOME_STUDENTE*'
    placeholder_date = '*DATA*'
    placeholder_parameters = ['*VALORE_A*', '*VALORE_B*', '*VALORE_C*', '*VALORE_D*']

    with open(template_path, 'r') as t:
        template_text = t.readlines()

    today = date.today()
    # dd/mm/YY
    today_date_str = today.strftime("%d/%m/%Y")

    test_text_lines = []

    for template_line in template_text:
        maybe_processed_line = replace_placeholder(template_line, placeholder_student_name, student_name)
        maybe_processed_line = replace_placeholder(maybe_processed_line, placeholder_date, today_date_str)
        for placeholder_param, coef in zip(placeholder_parameters, coeffs):
            maybe_processed_line = replace_placeholder(maybe_processed_line, placeholder_param, f"{coef}")
        test_text_lines.append(maybe_processed_line)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, f"test_{student_name}.html")

    md_input = ''.join(test_text_lines)
    convert_to_html(md_input, output_path)


def generate_tests(template_path: str, output_dir: str, student_lists: list, function_domain: tuple):
    e1, e2 = function_domain
    for student_name in student_lists:
        abcd_list = generate_abcd_omeo(e1, e2)
        generate_test_from_template(template_path, output_dir, abcd_list, student_name)


if __name__ == "__main__":
    studenti = ['alpha', 'beta', 'charlie']
    generate_tests("C:/dev/repos/funzione_omeografica_test/templates/test.md", "C:/dev/repos/funzione_omeografica_test/output", studenti, (-9, 10))