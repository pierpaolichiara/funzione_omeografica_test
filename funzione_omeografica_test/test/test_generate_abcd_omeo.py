import pytest
import funzione_omeografica_test.generate_abcd_omeo as mod
import hypothesis
from hypothesis import given
import hypothesis.strategies as st

#nei test limitiamo l'intervallo di appartenenza di e_min agli interi da -9 a 0, e di e_max da 1 a 9, per evitare i casi
# particolari della funzione 'generate_domain' che e' all'interno di 'generate_abcd_omeo', testata con test apposito.
@given(e_min=st.integers(min_value=-9, max_value=-1), e_max=st.integers(min_value=0, max_value=+9))
def test_c_generate_abcd_omeo(e_min: int, e_max: int):
    """
    Dati due estremi,
    il test verifica la C.N.S.1: che il coefficiente 'c' generato dalla funzione 'generate_abcd_omeo' a partire dagli estremi indicati
    sia diverso da zero.
    """
    [a,b,c,d]=mod.generate_abcd_omeo(e_min=e_min, e_max=e_max)
    assert c!=0

@given(e_min=st.integers(min_value=-9, max_value=-1), e_max=st.integers(min_value=0, max_value=+9))
def test_delta_generate_abcd_omeo(e_min: int, e_max: int):
    """
    Dati due estremi,
    il test verifica la C.N.S.2: che delta=a * d - c * b calcolato con i coefficeinti generati dalla funzione
    'generate_abcd_omeo' a partire dagli estremi indicati sia diverso da zero.
    """
    [a,b,c,d]=mod.generate_abcd_omeo(e_min=e_min, e_max=e_max)
    delta = a * d - c * b
    assert delta!=0

@given(e_min=st.integers(min_value=-9, max_value=-1), e_max=st.integers(min_value=0, max_value=+9))
def test_belong_generate_abcd_omeo(e_min: int, e_max: int):
    """
    Dati due estremi,
    il test verifica che i 4 coefficiente generati dalla funzione 'generate_abcd_omeo' a partire dagli estremi indicati
    appartengano al dominio con estremi in input inclusi.
    """
    [a, b, c, d] = mod.generate_abcd_omeo(e_min=e_min, e_max=e_max)
    coeffs = [a, b, c, d]
    domain=list(range(e_min,e_max+1))
    for coef in coeffs:
        assert coef in domain