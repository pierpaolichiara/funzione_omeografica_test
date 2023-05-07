import pytest
import funzione_omeografica_test.generate_abcd_omeo as lib

test_list = [
    [ "(2, 4)", (2, 4)],
    [ "(2,4)", (2, 4)],
    [ "(2,4 )", (2, 4)],
    [ "[2,4 )", (2, 4)],
    [ "[2,4 ]", (2, 4)],
    [ "2,3", (2, 3)],
    [ "-42,3", (-42, 3)],
    # [ "-42.5,3.0", (-42, 3)],
]
@pytest.mark.parametrize('input_str, expected_result', test_list)
def test_parse_function_domain(input_str, expected_result):
    input_values = input_str
    extrs = lib.parse_function_domain(input_values)
    assert extrs == expected_result

#TODO: idee di test
# controllare come fare se non voglio numeri relativi ma intervallo di reali o razionali
# controllare come escludere piu'di un valore
##test: genera_dominio(e,e)==dominio_vuoto
##test: genera_dominio(e+1,e)==dominio_vuoto  oppure e1>=e2
##test: genera_dominio(e,e+1)==[e]
##test: genera_dominio[0]==e1???????
##test  assert escludi in dominio==False  --> se metto ""???
##test: len(genera dominio(e1,e2))==abs(e1-e2)   #e2 escluso
##test: len(genera dominio(e1,e2,escludi))==abs(e1-e2)-1     #e2 escluso
##test: len(genera dominio(e1,e2,escludi))==len(genera dominio(-e2,-e1,escludi))
##test: type(genera_dominio(e1,e2))==str    if e1>=e2
##test: type(genera_dominio(e1,e2))==list   if e1<e2
##test:(genera_dominio(2.5, 3.1))==TypeError
##test

###i test vanno rivisti se il dominio e'un intervallo di numeri reali


def test_generate_domain():
    pass
    # assert lib.generate_domain()

def test_generate_abcd_omeo():
    pass
    # assert lib.generate_abcd_omeo()
