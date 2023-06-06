import os
import funzione_omeografica_test.get_output_folder_name as mod

def test_no_path_get_output_folder_name():
    """
    In assenza di input,
    il test verifica che la funzione 'get_output_folder_name' produca correttamente una cartella di 'output' all'interno
    della directory della libreria '..\funzione_omeografica_test'.
    """
    folder = ''
    output_folder = mod.get_output_folder_name(folder)
    assert output_folder == os.path.join(os.getcwd(), "output")

def test_rel_path_get_output_folder_name():
    """
    Dato un path relativo,
    il test verifica che la funzione 'get_output_folder_name' produca correttamente una cartella di output all'interno
    della directory della libreria '..\funzione_omeografica_test con il nome indicato in input.
    """
    folder = 'nomecartella'
    output_folder = mod.get_output_folder_name(folder)
    expected_output = os.path.join(os.getcwd(), "nomecartella")
    assert output_folder == expected_output

def test_abs_path_get_output_folder_name():
    """
    Dato un path assoluto,
    il test verifica che la funzione 'get_output_folder_name' produca correttamente una cartella di output nel path di input.
    """
    init_path = os.path.dirname(os.getcwd())
    input_path = os.path.join(init_path, "output_assoluto")
    output_folder = mod.get_output_folder_name(input_path)
    assert output_folder == input_path