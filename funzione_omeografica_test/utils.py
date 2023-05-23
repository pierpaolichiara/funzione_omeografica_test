import os


def get_output_folder(output_folder: str = None) -> str:  # indirizzo assoluto
    if output_folder:
        if os.path.isabs(output_folder):
            # se il path è assoluto (es. C:/Users/Matteo/...) lo prendiamo così com'è
            cartella_output = output_folder
        else:
            # altrimenti è un path relativo, e creiamo una sottocartella nella cartella dove l'utente esegue il comando
            current_working_dir = os.getcwd()
            cartella_output = os.path.join(current_working_dir, output_folder)
    else:
        # se l'utente non specifica nessuna cartella, creiamo una cartella di nome "output" nella cartella da cui l'utente
        # esegue il comando
        current_working_dir = os.getcwd()
        cartella_output = os.path.join(current_working_dir, "output")
    return cartella_output
