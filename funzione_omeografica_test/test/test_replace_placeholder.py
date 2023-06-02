import pytest
import funzione_omeografica_test.generate_tests as mod

input = [
            ['Lo studente *NOME_STUDENTE* oggi *DATA* prendera\' *VALORE_A*','' , '', 'Lo studente *NOME_STUDENTE* oggi *DATA* prendera\' *VALORE_A*' ],
            ['Lo studente *NOME_STUDENTE* oggi *DATA* prendera\' *VALORE_A*',  '*NOME_STUDENTE*', 'Enrico', 'Lo studente Enrico oggi *DATA* prendera\' *VALORE_A*'],
            ['Lo studente *NOME_STUDENTE* oggi *DATA* prendera\' *VALORE_A*',  '*DATA*', '28/05/2023', 'Lo studente *NOME_STUDENTE* oggi 28/05/2023 prendera\' *VALORE_A*'],
            ['Lo studente *NOME_STUDENTE* oggi *DATA* prendera\' *VALORE_A*',  '*VALORE_A*', '9', 'Lo studente *NOME_STUDENTE* oggi *DATA* prendera\' 9']
         ]
@pytest.mark.parametrize(('text, placeholder, value, expected_result'), input)
def test_replace_placeholder(text: str, placeholder: str, value: str, expected_result: str):
    """
    Dati un testo con un placeholder tra due asterischi, nome placeholder e valore da sostituire al placeholder nel testo,
    questo test verifica che la funzione 'replace_placeholder' sostituisca correttamente il placeholder e che quindi
    il testo fornito in output dalla funzione dopo la sostituzione sia quello previsto.
    """
    final_text=mod.replace_placeholder(text_line=text, placeholder_id=placeholder, placeholder_value=value)
    assert final_text==expected_result

