import pytest
import hypothesis
from hypothesis import given
import hypothesis.strategies as st

#import funzione_omeografica_test.generate_abcd_omeo as lib

def parse_function_domain(domain_extremes: str) -> tuple:
    extrs = [int(piece.strip("()[], ")) for piece in domain_extremes.split(",")]
    return tuple(extrs)
"""
@given(domain_extremes=st.floats())
def test_float(domain_extremes):
    extrs=parse_function_domain(domain_extremes)
    assert extrs == ValueError
"""

@given(domain_extremes=st.lists(st.floats()))
def test_float(domain_extremes):
    print(domain_extremes)
    domain_extremes_str = str(domain_extremes)
    with pytest.raises(ValueError):
        extrs = parse_function_domain(domain_extremes_str)