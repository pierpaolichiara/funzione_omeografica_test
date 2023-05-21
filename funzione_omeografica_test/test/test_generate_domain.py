import numpy as np
from numpy.testing import assert_array_equal
import pytest
import hypothesis
from hypothesis import given
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
    Dati due interi compresi tra -10 e 10,
    il test verifica che la funzione generate_domain genera il dominio corretto
    """
    if e1 >= e2:
        expected_error = ValueError
        with pytest.raises(expected_error):
            mod.generate_domain(e_min=e1, e_max=e2)
    else:
        domain = mod.generate_domain(e_min=e1, e_max=e2)
        assert domain == list(range(e1, e2+1))


@given(e1=st.integers(min_value=-10, max_value=+10),e2=st.integers(min_value=-10, max_value=+10),escludi=st.integers(min_value=-10, max_value=+10))
def test_lenght_generate_domain(e1,e2,escludi):
    if e1 < e2:
        if escludi is not None:
            if escludi in mod.generate_domain(e_min=e1, e_max=e2):
                assert len(mod.generate_domain(e_min=e1, e_max=e2, exclude_value=escludi)) == abs(e1-e2)
        else:
            assert len(mod.generate_domain(e_min=e1, e_max=e2, exclude_value=None)) == abs(e1-e2+1)


@given(e1=st.integers(min_value=-10, max_value=+10), e2=st.integers(min_value=-10, max_value=+10))
def test_reverse_generate_domain(e1, e2):
    """
    Dati due interi compresi tra -10 e 10,
    il test verifica che il dominio generato dalla funzione generate_domain sia opposto al dominio che si ottiene
    invertendo gli estremi e cambiandone il segno
    """
    if e1 < e2:
        list_pos=mod.generate_domain(e_min=e1, e_max=e2)
        list_neg=mod.generate_domain(e_min=-e2, e_max=-e1)
        vet_pos=np.array(list_pos)
        vet_neg=np.array(list_neg)
        assert_array_equal(vet_pos,-1*np.flip(vet_neg))
    return

    # assert lib.generate_domain()
# controllare cosa succede escludendo piu' di un valore
#generate_domain da rivedere perche' cambiata def di generate domain con estremo sup incluso


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