import pytest
import hypothesis
from hypothesis import given
import hypothesis.strategies as st
import funzione_omeografica_test.generate_abcd_omeo as mod

#@given(e_inf=st.integers(),e_sup=st.integers())
@given(e=st.integers())
def test_consecutive_extrs_generate_domain(e):
    assert mod.generate_domain(e_min=e,e_max=e+1)==[e,e+1]

@given(e1=st.integers(min_value=-10, max_value=+10),e2=st.integers(min_value=-10, max_value=+10))
def test_standard_generate_domain(e1,e2):
    if e1 < e2:
        assert mod.generate_domain(e_min=e1, e_max=e2) == list(range(e1, e2 + 1))

 #FIXME: caso e min > =  e max non funziona
"""
@given(e1=st.integers(min_value=-10, max_value=+10), e2=st.integers(min_value=-10, max_value=+10))
def test_standard_generate_domain(e1, e2, expected_result: ValueError):
    with pytest.raises(expected_result):
        if e1 >= e2:
            assert mod.generate_domain(e_min=e1, e_max=e2) == ValueError
"""

@given(e1=st.integers(min_value=-10, max_value=+10),e2=st.integers(min_value=-10, max_value=+10),escludi=st.integers(min_value=-10, max_value=+10))
def test_lenght_generate_domain(e1,e2,escludi):
    if e1 < e2:
        if escludi is not None:
            if escludi in mod.generate_domain(e_min=e1, e_max=e2):
                assert len(mod.generate_domain(e_min=e1, e_max=e2, exclude_value=escludi)) == abs(e1-e2)
        else:
            assert len(mod.generate_domain(e_min=e1, e_max=e2, exclude_value=None)) == abs(e1-e2+1)

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