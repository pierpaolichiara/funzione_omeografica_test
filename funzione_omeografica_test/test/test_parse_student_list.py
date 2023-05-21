import pandas as pd
import os
import hypothesis
import pytest
from hypothesis import given
import hypothesis.strategies as st
import funzione_omeografica_test.parse_student_list as mod

@given(path=st.text())
def test_not_path_parse_student_list(path:str):
    expected_error = IOError
    with pytest.raises(expected_error):
        assert mod.parse_student_list(path)

