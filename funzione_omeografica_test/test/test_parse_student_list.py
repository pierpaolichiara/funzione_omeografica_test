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


def test_xls_parse_student_list():
    """
    Dato un file excel esistente nel dispositivo in uso, esattamente il file nella cartella 'esempio_input',
    il test verifica che venga estratta la lista correta dei cognomi
    """
    this_file_path = os.path.abspath(__file__)
    xls_path = os.path.dirname(os.path.dirname(os.path.dirname(this_file_path)))
    print(xls_path)
    # TODO:nei sistemi operativi con / invece che \?mi da' un warning, inserire le righe sentro il test?
    names = os.path.join(xls_path, "esempio_input/CLASSE_1A.xlsx")
    print(names)
    lista=mod.parse_student_list(names)
    cognomi=['ALFA', 'BETA', 'CHARLIE', 'DELTA', 'ECHO', 'GOLF', 'INDIA', 'KILO', 'LIMA', 'MIKE', 'SIERRA', 'TANGO']
    assert lista==cognomi

#TODO: TEST PER CASO DI XLS VUOTO, CON SOLO TITOLO, CON LISTA IN PRIMA COLONNA
