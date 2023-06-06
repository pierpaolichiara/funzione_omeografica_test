import os
def empty_folder(folder_path: str):
    """
    Questa funzione rimuove tutti i file all'interno della cartella in input.

    Input
    -----
    folder_path: str
        indirizzo assoluto della cartella da svuotare
    """
    #utilizziamo questa funzione in 'generate_tests' dove e' gia' verificata la condizione di esistenza dell'input come path
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)