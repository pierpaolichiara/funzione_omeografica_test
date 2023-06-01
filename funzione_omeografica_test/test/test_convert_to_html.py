import pytest
import markdown
import funzione_omeografica_test.generate_tests as mod

def test_convert_to_html():
    """
    Fissata una stringa di testo,
    questo test verifica che la funzione 'convert_to_html' converta correttamente la stringa di testo da formato .md a .html
    """
    md_input_string = "# Verifica sullo studio di funzione omeografica\n" \
                      "\n" \
                      "2. Calcola, se esiste, il valore di `x` corrispondente all'asintoto verticale\n" \

    htm_output_file = "output.html"

    mod.convert_to_html(md_input_string, htm_output_file)

    with open(htm_output_file, 'r') as f:
        html_content = f.read()

    expected_html = '''<h1>Verifica sullo studio di funzione omeografica</h1>\n<ol>\n<li>Calcola, se esiste, il valore di <code>x</code> corrispondente all'asintoto verticale</li>\n</ol>'''

    assert html_content == expected_html