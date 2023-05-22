"""
#TODO: sistemare documentazione
Progetto per docenti di matematica delle scuole secondarie superiori:
Questo programma e' pensato per produrre test a risposta aperta sulla funzione 
omeografica f(x)=(ax +b)/(cx+d) da somministrare a una classe di studenti.
Ogni coefficiente della funzione viene scelto in maniera casuale all'interno 
di un intervallo di interi da specificare. A ogni alunno il programma associa una quaterna
di coefficienti [a,b,c,d] diversa, e per ogni alunno stampa il testo del test in formato html.
"""

import argparse
import os

from funzione_omeografica_test.generate_abcd_omeo import parse_function_domain
from funzione_omeografica_test.generate_tests import generate_tests
from funzione_omeografica_test.parse_student_list import parse_student_list
import pathlib

#TODO: controlla DESCRIZIONE
#assegnazione della cartella contenente il template del test da somministrare agli studenti da cui generare tutti i test
TEMPLATE_PATH = "../templates/test.md"

def get_output_folder(output_folder: str = None)->str:#indirizzo assoluto
    if output_folder:
        if os.path.isabs(output_folder):
            # se il path è assoluto (es. C:/Users/Matteo/...) lo prendiamo così com'è
            cartella_output = output_folder
        else:
            # altrimenti è un path relativo, e creiamo una sottocartella nella cartella dove l'utente esegue il comando
            current_working_dir = os.getcwd()
            cartella_output = os.path.join(current_working_dir, output_folder)
    else:
        #se l'utente non specifica nessuna cartella, creiamo una cartella di nome "output" nella cartella da cui l'utente
        # esegue il comando
        current_working_dir = os.getcwd()
        cartella_output = os.path.join(current_working_dir, "output")
    return cartella_output


def main():
    parser = argparse.ArgumentParser(description='Comando per generare test individuali sulla funzione omeografica.')
    parser.add_argument('-d', '--estremi_dominio', type=str, required=True, action='store',
                        help='Estremi del dominio da cui vengono estratti i parametri della funzione omeografica diversi per ogni studente.')
    parser.add_argument('-a', '--elenco_alunni', type=str, action='store', required=True,
                        help='File excel con elenco degli alunni per i quali generare il test')
    parser.add_argument('-o', '--cartella_output', type=str, action='store', required=False,

                        help='Cartella dove salvare i test generati automaticamente')
    args, _ = parser.parse_known_args()

#TODO: estremi. RIVEDERE NOMI ESTREMI CHIAMATI IN MODI DIVERSI NEI VARI FILE:
    # estremi_dominio, function_domain, extr, parse_function_domain(domain_extremes), e1, e2
    #TODO: sistemare linguaggio
    #assegno gli input ricevuti a delle variabili python, dopo averli resi in una forma piu' funzioanle al programma
    estremi_dominio = args.estremi_dominio
    print(estremi_dominio)
    estremi_dominio = parse_function_domain(estremi_dominio)
    file_elenco_alunni = args.elenco_alunni

    nomi_alunni = parse_student_list(file_elenco_alunni)

    # trova il path assoluto alla cartella dove si trova main.py
    base_dir = pathlib.Path(__file__).parent.resolve()

    # genera il path del template test.md
    template_test = os.path.join(base_dir, TEMPLATE_PATH)

    cartella_output = get_output_folder(args.cartella_output)
#todo: estremi
    generate_tests(template_test, cartella_output, nomi_alunni, estremi_dominio)


if __name__ == "__main__":
    main()
