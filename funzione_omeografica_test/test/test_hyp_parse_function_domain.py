import pytest
import hypothesis
from hypothesis import given
import hypothesis.strategies as st
import funzione_omeografica_test.generate_abcd_omeo as lib

@given(domain_extremes=st.lists(st.floats()))
def test_float_parse_function_domain(domain_extremes):
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