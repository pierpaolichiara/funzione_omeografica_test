"""
Progetto per docenti di matematica delle scuole secondarie superiori:
Questo programma e' pensato per produrre test a risposta aperta sulla funzione 
omeografica f(x)=(ax +b)/(cx+d) da somministrare a una classe di studenti.
Ogni coefficiente della funzione viene scelto in maniera casuale all'interno 
di un intervallo di interi da specificare in input. A ogni alunno il programma associa una quaterna
di coefficienti [a,b,c,d] diversa, e per ogni alunno stampa il testo del test in formato html.
"""

import argparse
from funzione_omeografica_test.generate_abcd_omeo import parse_function_domain
from funzione_omeografica_test.generate_tests import generate_tests
from funzione_omeografica_test.parse_student_list import parse_student_list
from funzione_omeografica_test.utils import get_output_folder
from funzione_omeografica_test.template_content_string import TEMPLATE_CONTENT


def main():
    #Utilizziamo 'parser' per analizzare gli input da linea di comando
    parser = argparse.ArgumentParser(description='Comando per generare test individuali sulla funzione omeografica.')
    parser.add_argument('-d', '--estremi_dominio', type=str, required=True, action='store',
                        help='Estremi del dominio da cui vengono estratti i parametri della funzione omeografica diversi per ogni studente.')
    parser.add_argument('-a', '--elenco_alunni', type=str, action='store', required=True,
                        help='File excel con elenco degli alunni per i quali generare il test')
    parser.add_argument('-o', '--cartella_output', type=str, action='store', required=False,
                        help='Cartella dove salvare i test generati automaticamente')
    #assegniamo a args.*** ogni dato *** in input riconosciuto
    args, _ = parser.parse_known_args()

    #assegniamo gli input ricevuti a delle variabili python, dopo averli resi in una forma piu' funzioanle al programma
    estremi_dominio = args.estremi_dominio
    print(estremi_dominio)
    estremi_dominio = parse_function_domain(domain_extremes=estremi_dominio)

    file_elenco_alunni = args.elenco_alunni
    nomi_alunni = parse_student_list(student_list_path=file_elenco_alunni)

    cartella_output = get_output_folder(output_folder=args.cartella_output)

    generate_tests(template_content_str=TEMPLATE_CONTENT, output_dir=cartella_output, student_lists=nomi_alunni, function_domain=estremi_dominio)


if __name__ == "__main__":
    main()
