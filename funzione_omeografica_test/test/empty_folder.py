def empty_folder(folder_path: str):
    """Questa funzione rimuove tutti i file all'interno della cartella in input."""
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)