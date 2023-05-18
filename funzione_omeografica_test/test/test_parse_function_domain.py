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
def test_parse_function_domain_raises(input_str, expected_result):
    with pytest.raises(expected_result):
        input_values = input_str
        extrs = lib.parse_function_domain(input_values)
        assert extrs == expected_result

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
