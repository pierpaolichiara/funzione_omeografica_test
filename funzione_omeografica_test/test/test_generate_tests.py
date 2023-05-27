import pytest
import os
import glob
import hypothesis
from hypothesis import given
import hypothesis.strategies as st
import funzione_omeografica_test.generate_tests as mod
#TODO: controlla se e'scritto bene il commento
#limitiamo il numero di elementi nelle liste e il numero di valori possibili degli interi per non mandare il computer in overflow
@given(text=st.text(alphabet=['0', '1', '2', '3', '+', '-', '.', ' ', '=', 'a', 'b', 'c'],
                    min_size=1,
                    max_size=3,
                    ),

       student_list=st.lists(st.text(min_size=1, max_size=5), min_size=4,max_size=7),

       extremes=st.tuples(st.integers(min_value=-3, max_value=-1),
                          st.integers(min_value=0, max_value=2)    #Il range di valori e' stato scelto in modo da garantire che il primo
                         )                                         # elemento della tupla sia strettamente minore del secondo,
      )                                                            # condizione necessaria per far girare  la funzione 'generate_abcd_omeo' in 'generate_tests'
                                                                   #Utilizziamo una tupla di 2 di interi perche':
                                                                    #  - e' il tipo di estremi che ci aspettiamo in input dall'utente
                                                                     #    e ci interessa verificare
                                                                     #  - e' il numero di estremi che ci aspettiamo in input dall'utente
                                                                     #    e ci interessa verificare


def test_generate_tests(text, student_list, extremes):
    current_working_dir = os.getcwd()
    cartella_output = os.path.join(current_working_dir, 'html_di_prova')
    mod.generate_tests(template_content_str=text, output_dir=cartella_output, student_lists=student_list, function_domain=extremes)

    #definiamo una funzione che ci conta il numero di files in una cartella perche' ci servira' per confrontare il
    # numero di file nella cartella di output con il numero di studenti nella lista
    def count_files_in_folder(folder_path:str)-> int:
        file_list = glob.glob(os.path.join(folder_path, '*'))
        return len(file_list)

    folder_path = cartella_output
    num_files = count_files_in_folder(folder_path)
  #  print(f"Il numero di file nella cartella {folder_path} è: {file_count}")
    assert len(student_list)==num_files