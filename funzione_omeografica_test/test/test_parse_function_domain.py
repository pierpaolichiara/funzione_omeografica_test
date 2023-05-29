import pytest
import hypothesis
from hypothesis import given
import hypothesis.strategies as st
import funzione_omeografica_test.generate_abcd_omeo as mod


#lista di liste di due elementi:
#- possibili stringhe in input,scritte sintatticamente in modo inappropriato dall'utente
#- tupla in output correttamente restituita da parse_function_domain
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
    Date delle stringhe di plausibili input, nonostante spazi in piu' o parentesi errate,
    il test verifica che la funzione parse_function_domain restituisca la tupla corretta
    """
    input_values = input_str
    extrs = mod.parse_function_domain(input_values)
    assert extrs == expected_result


#lista di liste di due elementi:
#- possibili stringhe in input, errate per tipo di dato o numero estremi inseriti
#- ValueError nell'esecuzione di parse_function_domain
test_list_no_int = [
    [ "-42.5,3.0", ValueError],     #test su inserimento di floats

 #   ["2,3,0", ValueError],         #test su inserimento di piu' di due estremi / di un intero scritto con la virgola
    [ "", ValueError],              #test su inserimento dominio vuoto
 #   [ "4", ValueError],             #test su inserimento di un solo estremo
    ["zero, 11", ValueError]        #test su inserimento di char
    ]
@pytest.mark.parametrize(('input_str, expected_result'), test_list_no_int)
def test_raises_parse_function_domain(input_str: str, expected_result: ValueError):
    """
    Date delle stringhe in input di tipo errato #FIXME o numero elementi errati,
    il test verifica che la funzione parse_function_domain riscontri un ValueError
    """
    with pytest.raises(expected_result):
        input_values = input_str
        extrs = mod.parse_function_domain(input_values)
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
        extrs = mod.parse_function_domain(domain_extremes_str)

@given(domain_extremes_list=st.lists(st.integers(), min_size=2, max_size=2))
#- utilizziamo una st.lists di interi perche' non esiste una st.str() che sarebbe
# il tipo di variabile di parse_function_domain
#- utilizziamo una st.lists di interi perche':
#        - e' il tipo di estremi che ci aspettiamo in input e ci interessa verificare
#        - per escludere dal test casi con eventuali errori di conversione
#          da lista a tupla dovuti al separatore dei decimali

def test_lenght_parse_function_domain(domain_extremes_list: list):
    """
    Data una lista di 2 interi,
    il test verifica che la tupla, associata alla lista convertita in stringa, generata da parse_function_domain
    abbia lunghezza 2.
    """
    # la nostra strategia prevede di passare una lista di 2 elementi, 'domain_extremes', perche' dobbiamo compararne
    # la lunghezza con quella della tupla generata dalla funzione 'parse_function_domain' che deve essere 2
    #if not len(domain_extremes_list) == 2:
     #   raise ValueError('Gli estremi inseriti non sono due. Per favore inserisci 2 estremi')
    #else:
    domain_extremes_str = str(domain_extremes_list)
    extrs = mod.parse_function_domain(domain_extremes_str)
    assert len(extrs)==2




