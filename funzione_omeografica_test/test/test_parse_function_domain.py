import pytest
import hypothesis
from hypothesis import given
import hypothesis.strategies as st
import funzione_omeografica_test.generate_abcd_omeo as lib

test_list = [
    [ "(2, 4)", (2, 4)],
    [ "(2,4)", (2, 4)],
    [ "(2,4 )", (2, 4)],
    [ "[2,4 )", (2, 4)],
    [ "[2,4 ]", (2, 4)],
    [ "2,3", (2, 3)],
    [ "-42,3", (-42, 3)],
]
@pytest.mark.parametrize(('input_str, expected_result'), test_list)
def test_parse_function_domain(input_str, expected_result):
    input_values = input_str
    extrs = lib.parse_function_domain(input_values)
    assert extrs == expected_result

test_list_no_int = [
    ( "-42.5,3.0", ValueError),
    ("42.1,3,0", ValueError),
    ("zero, 11", ValueError)
    ]

@pytest.mark.parametrize(('input_str, expected_result'), test_list_no_int)
def test_raises_parse_function_domain(input_str, expected_result):
    with pytest.raises(expected_result):
        input_values = input_str
        extrs = lib.parse_function_domain(input_values)
        assert extrs == expected_result


@given(domain_extremes=st.lists(st.floats()))
def test_floats_parse_function_domain(domain_extremes):
    """Data una lista di decimali il test verifica che la funzione parse_function_domain riscontri un ValueError"""
    print(domain_extremes)
    domain_extremes_str = str(domain_extremes)
    with pytest.raises(ValueError):
        extrs = lib.parse_function_domain(domain_extremes_str)

@given(domain_extremes=st.lists(st.integers(), #utilizziamo una lista di interi perche' e' l'input che ci aspettiamo
                                               # e che ci interessa verificare, e per escludere dal test casi con
                                               # eventuali errori di conversione da lista a tupla dovuti al separatore dei decimali
                                min_size=2,
                                max_size=2)
       )
def test_lenght_parse_function_domain(domain_extremes):
    """
    Data una lista di due interi, il test verifica che la tupla associata alla lista generata da parse_function_domain
    abbia lunghezza 2.
    """
    print(domain_extremes)
    domain_extremes_str = str(domain_extremes)
    extrs = lib.parse_function_domain(domain_extremes_str)
    assert len(extrs)==2

#TODO: idee di test

##test



#def test_generate_domain():

    # assert lib.generate_domain()
# controllare cosa succede escludendo piu' di un valore
#generate_domain da rivedere perche' cambiata def di generate domain con estremo sup incluso

##test: genera_dominio(e+1,e)==dominio_vuoto  oppure e1>e2
##test: genera_dominio(e,e)==[e]
##test: genera_dominio[0]==e1???????
##test  assert escludi in dominio==False  --> se metto ""???
##test: len(genera dominio(e1,e2))==abs(e1-e2+1)   #e2 incluso
##test: len(genera dominio(e1,e2,escludi))==abs(e1-e2)    #e2 incluso
##test: len(genera dominio(e1,e2,escludi))==len(genera dominio(-e2,-e1,escludi))
##test: type(genera_dominio(e1,e2))==str????ValueError    if e1>e2
##test: type(genera_dominio(e1,e2))==list   if e1<e2
##test:(genera_dominio(2.5, 3.1))==TypeError
#Sdef test_generate_abcd_omeo():
    #pass
    # assert lib.generate_abcd_omeo()
