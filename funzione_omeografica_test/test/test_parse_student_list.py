import pandas as pd
import os
import hypothesis
import pytest
from hypothesis import given
import hypothesis.strategies as st
import funzione_omeografica_test.parse_student_list as mod
import pathlib

@given(path=st.text())
def test_not_path_parse_student_list(path:str):
    """
    Data una stringa generica come input, che non e' un *.xls ne' un  *.xlsx,
    il test verifica che la funzione [parse_student_list](https://github.com/pierpaolichiara/funzione_omeografica_test/blob/main/funzione_omeografica_test/parse_student_list.py)
    fornisca il corretto tipo di errore.
    """
    expected_error = NameError
    with pytest.raises(expected_error):
        assert mod.parse_student_list(path)


def test_not_xls_parse_student_list():
    """
    Dato l'indirizzo assoluto del file corrente, che esiste ma non e' un *.xls ne' un  *.xlsx,
    il test verifica che la funzione parse_student_list fornisca il corretto tipo di errore
    """
    #ci serve un indirizzo assoluto di file esistente, e valido per test effettuati su ogni dispositivo:
    #utilizziamo l'indirizzo assoluto del file corrente, che e' in formato .py, nel dispositivo in uso
    es=os.path.abspath(__file__)
    expected_error = TypeError
    with pytest.raises(expected_error):
        assert mod.parse_student_list(es)

#selezioniamo due file all'interno del nostro pacchetto formattati e configurati in modo che il programma di generazione dei test funzioni
file_input=[ "esempio_input\CLASSE_5A.xlsx", "funzione_omeografica_test/test/excel_di_prova/COLONNA_D.xlsx"]
@pytest.mark.parametrize('path_input',file_input)
def test_xls_ok_parse_student_list(path_input: str):
    """
    Dato un file excel esistente nel dispositivo in uso, formattato nel modo richiesto dal programma,
    il test verifica che venga estratta la lista correta dei cognomi
    """
    this_file_path = os.path.abspath(__file__)
    xls_path = os.path.dirname(os.path.dirname(os.path.dirname(this_file_path)))
    # TODO:nei sistemi operativi con / invece che \?mi da' un warning,
    #  "DeprecationWarning: invalid escape sequence \C" inserire le righe sentro il test?
    names = os.path.join(xls_path, path_input)
    print(names)
    lista = mod.parse_student_list(names)
    cognomi = ['ALFA', 'BETA', 'CHARLIE', 'DELTA', 'ECHO', 'GOLF', 'INDIA', 'KILO', 'LIMA', 'MIKE', 'SIERRA',
              'TANGO']
    assert lista == cognomi

#selezioniamo due file all'interno del nostro pacchetto formattati e configurati in modo che il programma di generazione dei test funzioni
input=[("funzione_omeografica_test/test/excel_di_prova/ERR_TITOLO.xlsx", KeyError),
       ("funzione_omeografica_test/test/excel_di_prova/PRIMA_COL.xlsx", TypeError),
       ("funzione_omeografica_test/test/excel_di_prova/SOLO_TIT.xlsx", TypeError),
       ("funzione_omeografica_test/test/excel_di_prova/VUOTO.xlsx", TypeError)]

@pytest.mark.parametrize(('path_input, expected_error'), input)
def test_xls_raises_parse_student_list(path_input, expected_error):
    """
    Dati file excel non idonei come parametri della funzione 'parse_student_list',
    il test verifica che venga riportato all'utente un errore, accompagnato dal giusto messaggio di 'raise
    """
    this_file_path = os.path.abspath(__file__)
    xls_path = os.path.dirname(os.path.dirname(os.path.dirname(this_file_path)))
    # TODO:nei sistemi operativi con / invece che \?mi da' un warning,
    #  "DeprecationWarning: invalid escape sequence \C" inserire le righe sentro il test?
    names = os.path.join(xls_path, path_input)
    with pytest.raises(expected_error):
        assert mod.parse_student_list(names)