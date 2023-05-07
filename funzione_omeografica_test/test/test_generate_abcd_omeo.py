import pytest
import funzione_omeografica_test.assegna_abcd_omeo as lib

test_list = [
    [ "(2, 4)", (2, 4)],
    [ "(2,4)", (2, 4)],
    [ "(2,4 )", (2, 4)],
    [ "[2,4 )", (2, 4)],
    [ "[2,4 ]", (2, 4)],
    [ "2,3", (2, 3)],
    [ "-42,3", (-42, 3)],
    # [ "-42.5,3.0", (-42, 3)],
]
@pytest.mark.parametrize('input_str, expected_result', test_list)
def test_parse_function_domain(input_str, expected_result):
    input_values = input_str
    extrs = lib.parse_function_domain(input_values)
    assert extrs == expected_result

def test_generate_domain():
    pass
    # assert lib.generate_domain()

def test_generate_abcd_omeo():
    pass
    # assert lib.generate_abcd_omeo()
