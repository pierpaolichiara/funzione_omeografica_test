""" 
Progetto per docenti di matematica delle scuole secondarie superiori:
Questo programma e' pensato per produrre test a risposta aperta sulla funzione 
omeografica f(x)=(ax +b)/(cx+d) da somministrare a una classe di studenti.
Ogni coefficiente della funzione viene scelto in maniera casuale all'interno 
di un dominio da specificare. A ogni alunno il programma associa una quaterna 
di coefficienti [a,b,c,d] diversa, e per ogni alunno stampa il testo del test #in formato...##. 
L'associazione tra cognome dell'alunno e quaterna di coefficienti viene 
stampata su un file excel disponibile per l'insegnante

"""
import argparse
import os

from funzione_omeografica_test.genera_fz_omeografica import parse_function_domain, genera_fz_omeografica
from funzione_omeografica_test.lista import parse_student_list

def main():
    parser = argparse.ArgumentParser(description='Comando per generare test individuali sulla funzione omeografica.')
    parser.add_argument('-d', '--estremi_dominio', type=str, required=True, action='store', help='Estremi del dominio da cui vengono estratti i parametri della funzione omeografica diversi per ogni studenti.')
    parser.add_argument('-a', '--elenco_alunni', type=str, action='store', required=True, help='Elenco degli alunni per i quali generare il test')
    args, _ = parser.parse_known_args()

    estremi_dominio = args.estremi_dominio
    print(estremi_dominio)
    func_domain_extremes = parse_function_domain(estremi_dominio)

    file_elenco_alunni = args.elenco_alunni
    nomi_alunni = parse_student_list(file_elenco_alunni)
    print(nomi_alunni)

    # a, b, c, d = 1, 3, 5, 7
    # y = genera_fz_omeografica(a, b, c, d, )
    # print("f(x)=", y)


if __name__ == "__main__":
    main()


