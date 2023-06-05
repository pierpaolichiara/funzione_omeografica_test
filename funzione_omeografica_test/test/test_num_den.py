import sympy
from sympy import Symbol
from funzione_omeografica_test.generate_tests import num_den
import hypothesis
from hypothesis import given, assume, strategies as st

@given(coeffs=st.lists(st.integers(), min_size=4, max_size=4))
def test_type_num_den(coeffs: list):
    """
    Dati una lista di 4 interi compresi tra -20 e 20,
    questo test verifica che la funzione 'num_den' restituisca una tupla di due stringhe.
    """
    N, D = num_den(coeffs)
    assert type(num_den(coeffs)) == tuple
    assert type(N) == str
    assert type(D) == str

@given(coeffs=st.lists(st.integers(), min_size=4, max_size=4))
def test_star_num_den(coeffs: list):
    """
    Dati una lista di 4 interi compresi tra -20 e 20,
    questo test verifica che la funzione 'num_den' elimini gli asterischi '*' dai due elementi della tupla resituiti.
    """
    N, D = num_den(coeffs)
    for sym in N:
        assert 'sym' != '*'
    for sym in D:
        assert 'sym' != '*'

@given(coeffs=st.lists(st.integers(), min_size=4, max_size=4))
def test_bd_in_num_den(coeffs: list):
    """
    Dati una lista di 4 interi,
    assumendo che il secondo e il quarto siano diversi da 0,
    questo test verifica che i loro valori assoluti siano presenti rispettivamente nel primo e secondo elemento
    della tupla generata dalla funzione 'num_den'.
    """
    b,d = coeffs[1], coeffs[3]
    assume(b != 0)
    assume(d != 0)
    N, D = num_den(coeffs)
    #non facciamo in questo test verifiche sel primo e terzo elemento della lista perche' ci sarebbero da escludere
    # altri due casi da trattare a parte oltre lo zero (+1 e -1 che moltiplicano 'x')"
    assert str(abs(b)) in N
    assert str(abs(d)) in D