# -*- coding: utf-8 -*-
"""
Questa funzione restituisce una sequenza random di 4 coefficienti interi [a,b,c,d] 
appartenenti al dominio indicato in input, che verificano le condizioni necessarie per generare una funzione omeografica propria.

I coefficienti vengono scelti random con la funzione random.choice della libreria random, applicata alla sequenza in ingresso.

Vengono controllate le condizioni necessarie (C.N.) per l'esistenza di una funzione omeografica propria f(x)=(a*x+b)/(c*x+d)
associata alla quaterna dei coefficienti selezionati, che sono
 
   C.N.1:  c≠0 
   
   C.N.2:  a*d-c*b≠0
   
Qualora almeno una delle due C.N. non sia rispettata, viene generata una 
nuova sequenza di coefficienti e ricontrollate le C.N. fino a quando entrambe risultano verificate 
 
Parametri in input
------------------
dominio: list, insieme di interi da cui estrarre a, b, c, d
 
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


def parse_function_domain(domain_extremes: str) -> tuple:
    """"
    Riceve ad esempio "(2, 4)" da riga di comando e ritorna 2, 4
    """
    extrs = [int(piece.strip("()[], ")) for piece in domain_extremes.split(",")]
    return tuple(extrs)


def generate_domain(e1: int, e2: int, exclude_value:int = None) -> list:
    if e1 >= e2:
        raise ValueError("e2 deve essere strettamente maggiore di e1")

    domain = list(range(e1, e2))
    if exclude_value is not None:
        if exclude_value in domain:
            domain.remove(exclude_value)
        else:
            print(f"Non é possibile escludere {exclude_value} dal dominio perché non appartiene al dominio selezionato.")
    return domain


def generate_abcd_omeo(e1: int, e2: int) -> list:
    """
    Questa funzione genera un insieme di numeri interi relativi compresi tra
    e1(incluso) ed e2(escluso), ad esclusione al massimo di un numero denominato
    'escludi'.
    Se non si vuole eliminare nessun numero dall'intervallo non inserire 'escludi'

    Parametri in input
    ------------------
    e1: int, estremo sinistro dell'intervallo, compreso nello stesso
    e2: int, estremo destro dell'intervallo, non compreso nello stesso
    escludi: int, default=None, eventuale numero da escludere dall'intervallo

    Output
    ------
    list: se e1<e2, una sequenza di interi che parte da e1 incluso e si conclude
         con e2 escluso, eliminando al massimo un numero 'escludi' se compreso tra e1 ed e2

    oppure

    str: 'dominio_vuoto', se e1>=e2

    Esempi
    -------
    genera_dominio(-4,5,2)
    > [-4, -3, -2, -1, 0, 1, 3, 4]

    genera_dominio(-4,5)
    > [-4, -3, -2, -1, 0, 1, 2, 3, 4]

    genera_dominio(5,-4,2)
    > dominio vuoto

    genera_dominio(-4,5,6)
    > Non e' possibile escludere 6 dal dominio perche' non appartiene al dominio selezionato
    [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    """
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
