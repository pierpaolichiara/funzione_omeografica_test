import numpy as np
from numpy.testing import assert_array_equal
import pytest
import hypothesis
from hypothesis import given, assume
import hypothesis.strategies as st
import funzione_omeografica_test.generate_abcd_omeo as mod

@given(e=st.integers())
def test_same_extrs_generate_domain(e):
    """
    Dati due interi uguali come variabili,
    il test verifica che la funzione generate_domain restituisca un ValueError
    """
    expected_error = ValueError
    with pytest.raises(expected_error):
        assert mod.generate_domain(e_min=e,e_max=e)

#Qui e in seguito, limitiamo superiormente e inferiormente i valori di e1 ed e2 per evitare di andare incontro a un crush
# di pytest.
#In alternativa si potrebbe utilizzare un @settings(max_examples = ...),ma preferiamo la prima opzione perche' lavora su
# un set di interi piu' significativo ai fini del progetto

@given(e1=st.integers(min_value=-10, max_value=+10), e2=st.integers(min_value=-10, max_value=+10))
def test_basic_generate_domain(e1, e2):
    """
    Il test verifica che:
    dati due estremi interi compresi tra -10 e 10,
    quando il primo estremo e' minore del secondo,
    la funzione generate_domain genera il dominio corretto.
    """
    assume(e1<e2)
    domain = mod.generate_domain(e_min=e1, e_max=e2)
    assert domain == list(range(e1, e2+1))


@given(e1=st.integers(min_value=-10, max_value=+10), e2=st.integers(min_value=-10, max_value=+10))
def test_disordered_extrs_generate_domain(e1, e2):
    """
    Il test verifica che:
    dati due estremi interi compresi tra -10 e 10,
    quando il primo estremo e' maggiore o uguale al secondo,
    la funzione generate_domain restituisce l'errore corretto.
    """
    assume(e1>=e2)
    expected_error = ValueError
    with pytest.raises(expected_error):
        mod.generate_domain(e_min=e1, e_max=e2)

        
@given(e1=st.integers(min_value=-10, max_value=+10),e2=st.integers(min_value=-10, max_value=+10),escludi=st.integers(min_value=-10, max_value=+10))
def test_escludi_generate_domain(e1,e2,escludi):
    """
    Il test verifica che:
    dati 3 interi (e1,e2,escludi) compresi tra -10 e 10 tali che e1<e2,
    la funzione generate_domain genera il dominio corretto escludendo il numero 'escludi'.
    """
    assume(e1<e2)
    domain=mod.generate_domain(e_min=e1, e_max=e2, exclude_value=escludi)
    assert (escludi in domain) == False

@given(e1=st.integers(min_value=-10, max_value=+10),e2=st.integers(min_value=-10, max_value=+10),escludi=st.integers(min_value=-10, max_value=+10))
def test_lenght1_generate_domain(e1,e2,escludi):
    """
    Il test verifica che:
    dati 3 interi (e1,e2,escludi) compresi tra -10 e 10
    tali che e1<e2, quando escludiϵ[e1;e2],
    la funzione generate_domain genera un dominio con il corretto numero di elementi.
    """
    assume(e1<e2)
    assume(escludi in mod.generate_domain(e_min=e1, e_max=e2))
    assert len(mod.generate_domain(e_min=e1, e_max=e2, exclude_value=escludi)) == abs(e1-e2)

@given(e1=st.integers(min_value=-10, max_value=+10),e2=st.integers(min_value=-10, max_value=+10),escludi=st.integers(min_value=-10, max_value=+10))
def test_lenght2_generate_domain(e1,e2,escludi):
    """
    Il test verifica che:
    dati 3 interi (e1,e2,escludi) compresi tra -10 e 10
    tali che e1<e2, quando escludi∉[e1;e2],
    la funzione generate_domain genera un dominio con il corretto numero di elementi.
    """
    assume(e1<e2)
    assume(not escludi in mod.generate_domain(e_min=e1, e_max=e2))
    assert len(mod.generate_domain(e_min=e1, e_max=e2, exclude_value=None)) == abs(e1-e2)+1

@given(e1=st.integers(min_value=-10, max_value=+10), e2=st.integers(min_value=-10, max_value=+10))
def test_reverse_generate_domain(e1, e2):
    """
    Dati due interi compresi tra -10 e 10,
    il test verifica che il dominio generato dalla funzione generate_domain sia opposto al dominio che si ottiene
    invertendo gli estremi e cambiandone il segno
    """
    assume (e1<e2)
    list_pos=mod.generate_domain(e_min=e1, e_max=e2)
    list_neg=mod.generate_domain(e_min=-e2, e_max=-e1)
    vet_pos=np.array(list_pos)
    vet_neg=np.array(list_neg)
    assert_array_equal(vet_pos,-1*np.flip(vet_neg))
    return

