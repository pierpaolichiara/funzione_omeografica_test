import os

def get_output_folder(output_folder: str = None) -> str:  # indirizzo assoluto
    """"Questa funzione crea una cartella (cartella_output) vuota allo stesso livello del file corrente se l'input non esiste,
        altrimenti la crea a partire dall'input indicato.

        Input
        -----
        output_folder: str
            eventuale cartella di cui si verifica l'esistenza, inizializzata a None

        Output
        ------
        str:  cartella_output
        """
    if output_folder:
        if os.path.isabs(output_folder):
            # se il path è assoluto lo prendiamo così com'è
            cartella_output = output_folder
        else:
            # altrimenti è un path relativo, e creiamo una sottocartella nella cartella dove l'utente esegue il comando
            current_working_dir = os.getcwd()
            cartella_output = os.path.join(current_working_dir, output_folder)
    else:
        # se il path non esiste, non e' scritto correttamente o se l'utente non specifica nessuna cartella, creiamo una
        # cartella di nome "output" nella cartella da cui l'utente esegue il comando
        current_working_dir = os.getcwd()
        cartella_output = os.path.join(current_working_dir, "output")
    return cartella_output
