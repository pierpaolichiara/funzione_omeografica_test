import pytest
import hypothesis
from hypothesis import given
import hypothesis.strategies as st
import funzione_omeografica_test.generate_abcd_omeo as lib


#lista di liste di due elementi:
#- possibili stringhe in input,scritte sintatticamente in modo inappropriato dall'utente
#- tupla in output correttamente restituito da parse_function_domain
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
def test_parse_function_domain(input_str: str, expected_result:tuple):
    """
    Dati delle stringhe di plausibili input, nonostante spazi in piu' o parentesi errate,
    il test verifica che la funzione parse_function_domain restituisca la tupla corretta
    """
    input_values = input_str
    extrs = lib.parse_function_domain(input_values)
    assert extrs == expected_result


#lista di liste di due elementi:
#- possibili stringhe in input, errate per tipo di dato o numero estremi inseriti
#- ValueError nell'esecuzione di parse_function_domain
test_list_no_int = [
    [ "-42.5,3.0", ValueError],     #test su inserimento di floats
   #FIXME:test con 3 interi non funziona #TODO:sistemare test con 3 interi
  # ["42,3,0", ValueError],         #test su inserimento di piu' di due estremi / di un intero scritto con la virgola
    ["zero, 11", ValueError]        #test su inserimento di char
    ]
@pytest.mark.parametrize(('input_str, expected_result'), test_list_no_int)
def test_raises_parse_function_domain(input_str: str, expected_result: ValueError):
    """
        Date delle stringhe in input di tipologia o numero elementi errati,
        il test verifica che eseguedo la funzione parse_function_domain riscontri un ValueError
        """
    with pytest.raises(expected_result):
        input_values = input_str
        extrs = lib.parse_function_domain(input_values)
        assert extrs == expected_result


@given(domain_extremes=st.lists(st.floats()))
def test_floats_parse_function_domain(domain_extremes):
    """
    Data una lista di decimali,
    il test verifica che la funzione parse_function_domain riscontri un ValueError
    """
    print(domain_extremes)
    domain_extremes_str = str(domain_extremes)
    with pytest.raises(ValueError):
        extrs = lib.parse_function_domain(domain_extremes_str)

@given(domain_extremes=st.lists(st.integers(), #- utilizziamo una st.lists perche' non esiste una st.str() che sarebbe
                                               # il tipo di variabile di parse_function_domain
                                               #- utilizziamo una st.lists di interi perche':
                                               #        - e' il tipo di estremi che ci aspettiamo in input e ci interessa verificare
                                               #        - per escludere dal test casi con eventuali errori di conversione
                                               #          da lista a tupla dovuti al separatore dei decimali
                                min_size=2,
                                max_size=2)
       )
def test_lenght_parse_function_domain(domain_extremes: list):
    """
    Data una lista di due interi,
    il test verifica che la tupla, associata alla lista convertita in stringa, generata da parse_function_domain abbia lunghezza 2.
    """
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
