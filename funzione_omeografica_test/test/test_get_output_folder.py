import os
import funzione_omeografica_test.get_output_folder as mod

def test_get_output_folder():
    """Dato il percorso di una cartella,
    il test verifica che la funzione 'get_output_folder' produca corettamente una cartella di 'output' all'interno
    della directory della libreria '..\funzione_omeografica_test'."""

    # Test1: nessun input
    folder = ''
    output_folder = mod.get_output_folder(folder)
    assert output_folder == os.path.join(os.getcwd(), "output")

    # Test2: input = path relativo
    folder = 'nomecartella'
    output_folder = mod.get_output_folder(folder)
    expected_output = os.path.join(os.getcwd(), "nomecartella")
    assert output_folder == expected_output

    # Test case 3: input = path assoluto
    init_path = os.path.dirname(os.getcwd())
    input_path = os.path.join(init_path, "output_assoluto")
    output_folder = mod.get_output_folder(input_path)
    assert output_folder == input_path