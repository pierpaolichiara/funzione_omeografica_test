import pytest
import os
import glob
import funzione_omeografica_test.generate_tests as mod
from funzione_omeografica_test.empty_folder import empty_folder
from hypothesis import given, assume, strategies as st

#Abbiamo provato a estarre la funzione generate_test inserendo (template_content_str, student list, function domain)
#parametrizzati con hypothesis, ma si e'preferito procedere qui con pochi casi mirati al sovraccarico di calcolo
# di tutte le combinazioni possibili degli input con hypothesis


#definiamo una funzione che ci conta il numero di files in una cartella perche' ci servira' per confrontare il
# numero di file nella cartella di output con il numero di studenti nella lista
def count_files_in_folder(folder_path: str) -> int:
    """Questa funzione conta i file contenuti in una cartella.
    Input:
    -----
    folder_path: str
        indirizzo assoluto della cartella

    Output
    ------
    num: int
        numero di file contati nella cartella di input
    """
    #creiamo una lista di percorsi di file che si trovano nella cartella in input: ci serve la lista per contarne
    # gli elementi
    file_list = glob.glob(os.path.join(folder_path, '*'))
    return len(file_list)


input= [
    [["chiara", "enrico", "giampiero"], (-3, 3)],
    [[],(0,3) ],
    [["chiara"],(1,2) ]
]

@pytest.mark.parametrize(('student_list, extremes'),input)
def test_num_generate_tests(student_list, extremes):
    """
    Data una lista di nomi e una tupla di estremi interi, con estremo sinistro<estremo destro,
    questa funzione controlla che i test generati da 'generate_tests' a partire dai dati in input siano in numero uguale
    alla lunghezza della lista in input.
    """
    current_working_dir = os.getcwd()
    cartella_output = os.path.join(current_working_dir, 'html_di_prova')
    # e' necessario svuotare la cartella_output ogni volta che il test viene eseguito su una lista di quelle in input
    # perche' se la cartella esisteva gia' perche' creata in un test precedente, i test generati nella sessione corrente
    # si sommerebbero a quelli creati a partire dalla lista in input precedente, e il valore num_files sarebbe quindi
    #non legato a un input ma cumulativo di tutti gli input
    empty_folder(cartella_output)
    text='0+. -abc{}'
    class_id="5A"
    mod.generate_tests(template_content_str=text, output_dir=cartella_output, student_lists=student_list, function_domain=extremes, class_id=class_id)
    num_files = count_files_in_folder(cartella_output)
    empty_folder(cartella_output)
    assert len(student_list) == num_files



input=  [
        (["student1", "student2"], "class1", (-10, 10)),
        (["student3", "student4"], "class2", (11, 20))
        ]
@pytest.mark.parametrize("student_list, class_id, extremes", input)
def test_filename_generate_tests(student_list, class_id, extremes, tmp_path):
    """
    Data una lista di nomi e un suo codice identificativo, una tupla di estremi interi, con estremo sinistro<estremo destro,
    questa funzione controlla che i test generati da 'generate_tests' vengano salvati col nome giusto nella cartella corretta.
    """
    cartella_output = tmp_path / "test_output"
    cartella_output.mkdir()
    text = '0+. -abc{}'
    mod.generate_tests(template_content_str=text, output_dir=str(cartella_output), student_lists=student_list,
                       function_domain=extremes, class_id=class_id)

    for student_name in student_list:
        path = cartella_output / f'test_{class_id}_{student_name}.html'
        assert path.exists()