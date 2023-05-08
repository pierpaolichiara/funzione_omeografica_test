# -*- coding: utf-8 -*-
"""
Questo modulo restituisce una sequenza random di 4 coefficienti interi [a,b,c,d]
appartenenti al dominio indicato in input, che verificano le condizioni necessarie e sufficienti per
generare una funzione omeografica propria.

I coefficienti vengono scelti random con la funzione random.choice della libreria random, applicata alla sequenza
in ingresso.

Vengono controllate le condizioni necessarie e sufficienti (C.N.S) per l'esistenza di una funzione omeografica propria
    f(x)=(a*x+b)/(c*x+d)
associata alla quaterna dei coefficienti selezionati, che sono
 
   C.N.S.1:  c≠0
   
   C.N.S.2:  a*d-c*b≠0
   
Qualora almeno una delle due C.N.S. non sia rispettata, viene generata una
nuova sequenza di coefficienti e ricontrollate le C.N.S. fino a quando entrambe risultano verificate
 
Input
------------------
dominio: list
    insieme di interi da cui estrarre a, b, c, d
 
Output
-------
[a,b,c,d]: list 
    sequenza di 4 coefficienti interi appartenenti a dominio in input, idonei a generare una funzione omeografica propria 
 
Raises ###??? TRADUZIONE?
------
 
 
Vedi anche
----------
#TODO    random.choice 
dominio_int.genera_dominio

"""

import random

def parse_function_domain(domain_extremes: str) -> tuple:  #PERCHE' UNA TUPLA? VEDI SPLIT
    """
    Riceve gli estremi dell'intervallo di interi da considerare e li associa ad una tupla.
    Evita di richiedere gli estremi separatamente e garantisce la definizione del dominio attraverso un unico elemento tupla

    Input
    -----
    domain_extremes: str   #TODO MEGLIO RICHIEDERE STRINGA DI INT????
        i due estremi del dominio da considerare, se non di tipo int vengono convertiti a interi

    Output
    ------
    tuple: tupla con due elementi
       Es. (-9,10)

    Esempi
    ------
    >>> parse_function_domain(-9,10)
    (-9,10)
    >>> parse_function_domain("(-9,10)")
    (-9,10)
    >>> parse_function_domain("[-9,10]")
    (-9,10)

    """
    extrs = [int(piece.strip("()[], ")) for piece in domain_extremes.split(",")]
    return tuple(extrs)


def generate_domain(e1: int, e2: int, exclude_value: int = None) -> list:
    """
    Questa funzione genera un insieme di numeri interi relativi compresi tra
    e1(incluso) ed e2(escluso), ad esclusione al massimo di un numero denominato
    exclude_value.
    Se non si vuole eliminare nessun numero dall'intervallo non inserire exclude_value.

    Input
    ------
    e1: int
        estremo sinistro dell'intervallo, compreso nello stesso
    e2: int
        estremo destro dell'intervallo, non compreso nello stesso
    exclude_value: int, default=None
        eventuale numero da escludere dall'intervallo

    Output
    ------
    list: [e1, e1+1, e1+2, ..., e2-2, e2-1]
          se e1<e2, una sequenza di interi che parte da e1 incluso e si conclude
          con e2 escluso, eliminando al massimo un numero exclude_value se compreso tra e1 ed e2

    Raises
    ------
    e1>=e2:    "ValueError: e2 deve essere strettamente maggiore di e1"
    exclude_value<e1 oppure exclude_value>=e2:
               "Warning: Non é possibile escludere {exclude_value} dal dominio perché non appartiene al dominio selezionato

    Esempi
    -------
    generate_domain(-4,5,2)
    > [-4, -3, -2, -1, 0, 1, 3, 4]

    generate_domain(-4,5)
    > [-4, -3, -2, -1, 0, 1, 2, 3, 4]

    generate_domain(5,-4,2)
    > ValueError: e2 deve essere strettamente maggiore di e1

    generate_domain(-5,4, 22)
    > Non é possibile escludere 22 dal dominio perché non appartiene al dominio selezionato.
    > [-5, -4, -3, -2, -1, 0, 1, 2, 3]
    """
    if e1 >= e2:
        raise ValueError("e2 deve essere strettamente maggiore di e1")

    domain = list(range(e1, e2))
    if exclude_value is not None:
        if exclude_value in domain:
            domain.remove(exclude_value)
        else:
            print(f"Warning: Non é possibile escludere {exclude_value} dal dominio perché non appartiene al dominio selezionato.")
    return domain


def generate_abcd_omeo(e1: int, e2: int) -> list:

    domain_abd = generate_domain(e1, e2)
    # verifica C.N.1
    domain_c = generate_domain(e1, e2, 0)

    delta = 0
    a = b = c = d = None
    while delta == 0:  # verifica C.N.2
        a = random.choice(domain_abd)
        b = random.choice(domain_abd)
        c = random.choice(domain_c)
        d = random.choice(domain_abd)
        delta = a * d - c * b

    return [a, b, c, d]


if __name__ == "__main__":
    for _ in range(10):
        abcd = generate_abcd_omeo(-9, 10)
        print('i coefficienti sono [a,b,c,d]=', abcd)
