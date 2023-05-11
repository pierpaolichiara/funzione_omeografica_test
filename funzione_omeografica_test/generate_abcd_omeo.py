# -*- coding: utf-8 -*-
"""
Questo modulo restituisce una sequenza random di 4 coefficienti interi [a,b,c,d]
appartenenti al dominio indicato in input, che verificano le condizioni necessarie e sufficienti per
generare una funzione omeografica propria.

I coefficienti vengono scelti random con la funzione random.choice della libreria random.

Vengono controllate le condizioni necessarie e sufficienti (C.N.S) per l'esistenza di una funzione omeografica propria
    f(x)=(a*x+b)/(c*x+d)
associata alla quaterna dei coefficienti selezionati, che sono
 
   C.N.S.1:  c≠0
   
   C.N.S.2:  a*d-c*b≠0
   
Qualora almeno una delle due C.N.S. non sia rispettata, viene generata una
nuova sequenza di coefficienti e ricontrollate le C.N.S. fino a quando entrambe risultano verificate
"""

import random

def parse_function_domain(domain_extremes: str) -> tuple:  # PERCHE' UNA TUPLA? VEDI SPLIT
    """
    Riceve una stringa con gli estremi dell'intervallo di interi da considerare e li associa ad una tupla.
    Evita di richiedere gli estremi separatamente e garantisce la definizione del dominio attraverso un unico elemento
    tupla definito all'inizio dell'esecuzione e non modificabile

    Input
    -----
    domain_extremes: str   #TODO: MEGLIO RICHIEDERE STRINGA DI INT????
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

    #TODO: ERRORE, casi con float: dovrebbe convertire ad intero? o dare errore?
    """
    extrs = [int(piece.strip("()[], ")) for piece in domain_extremes.split(",")]
    return tuple(extrs)


print(parse_function_domain("(-9,9,0)"))

def generate_domain(e1: int, e2: int, exclude_value: int = None) -> list:
    """
    Questa funzione genera un insieme di numeri interi relativi compresi tra
    e1(incluso) ed e2(incluso), ad esclusione al massimo di un numero denominato
    exclude_value.
    Se non si vuole eliminare nessun numero dall'intervallo non inserire exclude_value.

    Input
    ------
    e1: int
        estremo sinistro dell'intervallo, compreso nello stesso
    e2: int
        estremo destro dell'intervallo, compreso nello stesso
    exclude_value: int, default=None
        eventuale numero da escludere dall'intervallo

    Output
    ------
    list: [e1, e1+1, e1+2, ..., e2-2, e2]
          se e1<=e2, e' una sequenza di interi che parte da e1 incluso e si conclude
          con e2 incluso, eliminando al massimo un numero exclude_value se compreso tra e1 ed e2

    Raises
    ------
    e1>e2:    "ValueError: e2 deve essere maggiore o uguale a e1"
    exclude_value<e1 oppure exclude_value>e2:
              "Warning: Non é possibile escludere {exclude_value} dal dominio perché non appartiene al dominio selezionato

    Esempi
    ------
    generate_domain(-4,5,2)
    >>> [-4, -3, -2, -1, 0, 1, 3, 4, 5]

    generate_domain(-4,5)
    >>> [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

    generate_domain(5,-4,2)
    >>> ValueError: e2 deve essere maggiore o uguale a e1

    generate_domain(-5,4, 22)
    >>> Warning: Non é possibile escludere 22 dal dominio perché non appartiene al dominio selezionato.
    >>> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
    """
    if e1 > e2:
        raise ValueError("e2 deve essere maggiore o uguale a e1")

    domain = list(range(e1, e2+1))
    if exclude_value is not None:
        if exclude_value in domain:
            domain.remove(exclude_value)
        else:
            #TODO: si puo'fare un raise Warning?
            raise Warning(f"Non é possibile escludere {exclude_value} dal dominio perché non appartiene al dominio selezionato.")
    return domain


#    print(generate_domain(5, 4, 22))

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
        estremo sinistro del dominio da cui estrarre i coefficienti
    e2: int
        estremo destro del dominio da cui estrarre i coefficienti

    Output
    ------
    list: [a, b, c, d]
        lista dei quattro coefficienti estratti random dal dominio definito in input
    """
    #calcolo dominio
    domain_abd  = generate_domain(e1, e2)
    # verifica C.N.1
    domain_c = generate_domain(e1, e2, 0)
    #inizializzazione parametriper essere sicuri di avere un return se il ciclo non dovesse essere svolto
    delta = 0
    a = b = c = d = None
    # verifica C.N.2
    while delta == 0:
        #assegnazione random ai coefficienti
        a = random.choice(domain_abd)
        b = random.choice(domain_abd)
        c = random.choice(domain_c)
        d = random.choice(domain_abd)
        delta = a * d - c * b
    return [a, b, c, d]

#print(generate_abcd_omeo(-2,4))

if __name__ == "__main__":  # TODO: VA BENE QUI?
   for _ in range(10):  #TODO: Perche'10?
       abcd = generate_abcd_omeo(e1, e2)    #controllare se va bene o extrs
       print('i coefficienti sono [a,b,c,d]=', abcd)

