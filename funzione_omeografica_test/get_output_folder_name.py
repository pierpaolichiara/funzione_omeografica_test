import os

def get_output_folder_name(output_folder_path: str = None) -> str:
    """"Questa funzione crea il nome di una cartella (cartella_output) vuota allo stesso livello del file corrente se l'input non esiste,
        altrimenti lo crea a partire dall'input indicato.

        Input
        -----
        output_folder_path: str
            eventuale cartella di cui si verifica l'esistenza, inizializzata a None

        Output
        ------
        str:  cartella_output
        """
    if output_folder_path:
        if os.path.isabs(output_folder_path):
            # se il path è assoluto lo prendiamo così com'è
            cartella_output = output_folder_path
        else:
            # altrimenti è un path relativo:creiamo una sottocartella nella cartella dove l'utente esegue il comando
            # che termina con il path indicato
            current_working_dir = os.getcwd()
            cartella_output = os.path.join(current_working_dir, output_folder_path)
    else:
        # se il path non esiste, non e' scritto correttamente o se l'utente non specifica nessuna cartella, creiamo una
        # sottocartella di nome "output" nella cartella da cui l'utente esegue il comando
        current_working_dir = os.getcwd()
        cartella_output = os.path.join(current_working_dir, "output")
    print(f"I test verranno salvati in {cartella_output}")
    return cartella_output
