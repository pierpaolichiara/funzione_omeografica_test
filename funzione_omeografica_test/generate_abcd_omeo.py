# -*- coding: utf-8 -*-
"""
Questo modulo restituisce una sequenza di 4 coefficienti interi [a,b,c,d]
appartenenti al dominio indicato in input e scelti in maniera casuale, che verificano le condizioni necessarie e sufficienti per
generare una funzione omeografica propria.

I coefficienti vengono scelti random con la funzione random.choice della libreria random.

Vengono controllate le condizioni necessarie e sufficienti (C.N.S.1 e 2) per l'esistenza di una funzione omeografica propria
    f(x)=(a*x+b)/(c*x+d)
associata alla quaterna dei coefficienti selezionati, che sono
 
   C.N.S.1:  c≠0
   
   C.N.S.2:  a*d-c*b≠0
   
Qualora almeno una delle due C.N.S. non sia rispettata, viene generata una
nuova sequenza di coefficienti e ricontrollate le C.N.S. fino a quando entrambe risultano verificate
"""

import random
#TODO:estremi
def parse_function_domain(domain_extremes: str) -> tuple:  # PERCHE' UNA TUPLA? VEDI SPLIT
    """
    Riceve una stringa con gli estremi dell'intervallo di interi da considerare e li associa ad una tupla.
    Evita di richiedere gli estremi separatamente e garantisce la definizione del dominio attraverso un unico elemento
    tupla definito all'inizio dell'esecuzione e non modificabile

    Input
    -----
    domain_extremes: str
        i due estremi del dominio da considerare, se non di tipo int vengono convertiti a interi

    Output
    ------
    tuple: tupla di due elementi
        i due elementi sono gli estremi del dominio in input

    Raises
    ------
    ValueError: invalid literal for int() with base 10: '-9.1'
        se si inserisce un numero non 'int'

    Esempi
    ------
    >>> parse_function_domain(-9,10)
    (-9,10)
    >>> parse_function_domain("(-9,10)")
    (-9,10)
    >>> parse_function_domain("[-9,10]")
    (-9,10)
    >>> parse_function_domain("[-9.1,10]")
    ValueError: invalid literal for int() with base 10: '-9.1'
    >>> parse_function_domain("(-9,9,0)")
    ValueError: invalid literal for int() with base 10: '-9.1'

    """
    extrs = [int(piece.strip("()[], ")) for piece in domain_extremes.split(",")]
    return tuple(extrs)


#print(parse_function_domain("(-9,9,0)"))

#TODO:estremi
def generate_domain(e_min: int, e_max: int, exclude_value: int = None) -> list:
    """
    Questa funzione genera un insieme di numeri interi relativi compresi tra
    e_min(incluso) ed e_max(incluso), ad esclusione al massimo di un numero denominato
    exclude_value.
    Se non si vuole eliminare nessun numero dall'intervallo non inserire exclude_value.
    Se exclude_value e' esterno all'intervallo inserito, compare un warning, ma il dominio viene comuuque generato.

    Input
    ------
    e_min: int
        estremo sinistro dell'intervallo, compreso nello stesso
    e_max: int
        estremo destro dell'intervallo, compreso nello stesso e maggiore di e_min
    exclude_value: int, default=None
        eventuale numero da escludere dall'intervallo

    Output
    ------
    list: [e_min, e_min+1, e_min+2, ..., e_max-1, e_max]
          se e_min<e2, e' una sequenza di interi che parte da e1 incluso e si conclude
          con e2 incluso, eliminando al massimo un numero exclude_value se compreso o uguale a tra e_min ed e2

    Raises
    ------
    e_min>=e_max:    "ValueError: e_max deve essere maggiore di e_min"
    exclude_value<e_min oppure exclude_value>e_max:
              "Warning: Non é possibile escludere {exclude_value} dal dominio perché non appartiene al dominio selezionato

    Esempi
    ------
    generate_domain(-4,5,2)
    >>> [-4, -3, -2, -1, 0, 1, 3, 4, 5]

    generate_domain(-4,5)
    >>> [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

    generate_domain(5,-4,2)
    >>> ValueError: e_max deve essere maggiore di e_min

    generate_domain(-5,4, 22)
    >>> Warning: Non é possibile escludere 22 dal dominio perché non appartiene al dominio selezionato.
    >>> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
    """
    if e_min >= e_max:
        raise ValueError("e_max deve essere maggiore di e_min")

    domain = list(range(e_min, e_max+1))
    if exclude_value is not None:
        if exclude_value in domain:
            domain.remove(exclude_value)
        else:
            #si potrebbe inserire un 'raise Warning', ma a quel punto la funzione non verrebbe calcolata
            print(f"Warning:Non é possibile escludere {exclude_value} dal dominio perché non appartiene al dominio selezionato.")
    return domain


#    print(generate_domain(5, 4, 22))
#TODO:estremi
def generate_abcd_omeo(e1: int, e2: int) -> list:
    """
    Questa funzione genera una lista di 4 coefficienti interi [a, b, c, d] in grado di dare origine a una funzione omeografica propria
    del tipo f(x)=(ax+b)/(cx+d).
    In particolare i 4 coefficienti:
    - appartengono al dominio di estremi specificati in input
    - vengono scelti con la funzione random.choice dal dominio
    - verificano le due condizioni necessarie e sufficienti (C.N.S.) per dare origine a una funzione omeografica propria:

        C.N.S.1:  c≠0

        C.N.S.2:  a*d-c*b≠0

    Input
    -----
    e1: int
        estremo inferiore del dominio da cui estrarre i coefficienti
    e2: int
        estremo superiore del dominio da cui estrarre i coefficienti

    Output
    ------
    list: [a, b, c, d]
        lista dei quattro coefficienti estratti random dal dominio definito in input

    Vedi  #TODO: LINK A generate_domain e random_choice()
    ----
    generate_domain(e1, e2)
    random_choice()
    """
    #calcolo dominio:
    domain_abd  = generate_domain(e1, e2)
    #assegnazione C.N.1
    domain_c = generate_domain(e1, e2, 0)
    #inizializzazione parametri per essere sicuri di avere un return se il ciclo non dovesse essere svolto
    delta = 0
    a = b = c = d = None
    #verifica C.N.2
    while delta == 0:
        #assegnazione random ai coefficienti: la scelta random permette di uscire sicuramente dal ciclo dopo un certo
        #numero finito di iterazioni dello stesso perche' la probabilita' di avere un delta sempre uguale a 0 e' non
        #nulla per un dominio di almeno due numeri interi diversi.
        #Utilizzare la funzione generate_domain in cui i due estremi sono diversi, ci garantisce che il dominio non e'
        # un solo numero, caso che produrrebbe un delta=0
        a = random.choice(domain_abd)
        b = random.choice(domain_abd)
        d = random.choice(domain_abd)
        c = random.choice(domain_c)

        delta = a * d - c * b
    return [a, b, c, d]

#print(generate_abcd_omeo(-2,4))

#TODO:estremi
if __name__ == "__main__":  # TODO: VA BENE QUI?
   for _ in range(10):  #TODO: Perche'10?
       abcd = generate_abcd_omeo(-9, 9)    #controllare se va bene o extrs
       print('i coefficienti sono [a,b,c,d]=', abcd)

