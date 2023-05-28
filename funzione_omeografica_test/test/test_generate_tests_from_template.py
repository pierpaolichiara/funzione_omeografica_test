import pytest
import os
import funzione_omeografica_test.generate_tests as mod

input=[
        [ [0,0,0,0], "ZERO" ],
        [ [1,'',1,-1], "bVUOTO" ],
        [ [-3,0,9,-7], "ENRICO" ]
       ]

#in questo test per la funzione 'generate_test_from_template',teniamo fissi
# - il parametro 'template_content_str' perche' nella nostra libreria e' gia' fissato (ne testiamo un estratto significativo)
# - il parametro 'output_dir' per poter inserire tutti i file generati dentro la cartella fissata (anche nel main,
#       quando viene chiamata la funzione, l'output_dir e' gia' fissata ed esistente

text = "Verifica: *NOME_STUDENTE*, [a,b,c,d]=['*VALORE_A*','*VALORE_B*','*VALORE_C*','*VALORE_D*']"
cartella_output = os.path.join(os.getcwd(), 'generate_test_from_template_prova')
@pytest.mark.parametrize(('abcd, name'),input)
def test_generate_test_from_template(abcd: list, name: str):
    """
    Fissati una stringa di testo e una cartella, dati una lista di 4 interi e un nome variabili,
    il test verifica che la funzione generate_test_from_template generi correttamente un file .html nella cartella fissata,
    sostituendo, se presenti, i segnaposto con i valori in input.
    """
    mod.generate_test_from_template(template_content_str=text, output_dir=cartella_output, coeffs=abcd, student_name=name)
    file_html=os.path.join(cartella_output, f"test_{name}.html")
    with open(file_html, 'r') as f:
        html_content = f.read()
    expected_html = f'''<p>Verifica: {name}, [a,b,c,d]=['{abcd[0]}','{abcd[1]}','{abcd[2]}','{abcd[3]}']</p>'''
    assert expected_html==html_content

