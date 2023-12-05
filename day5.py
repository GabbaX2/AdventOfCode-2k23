import sys
from typing import List, Tuple

FILE = sys.argv[1] if len(sys.argv) > 1 else "day5.in"


def leggi_righe_in_lista() -> List[str]:
    righe: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for riga in f:
            riga = riga.strip()
            righe.append(riga)

    return righe


def leggi_mappa(righe: List[str]) -> List[Tuple[range, int]]:
    mappatura = []

    if len(righe) == 0:
        return mappatura
    righe.pop(0)

    while len(righe) > 0 and len(righe[0]) > 0:
        riga = righe.pop(0)
        [destinazione, inizio, lunghezza] = [int(valore) for valore in riga.split()]
        mappatura.append((range(inizio, inizio + lunghezza), destinazione))

    if len(righe) > 0:
        righe.pop(0)

    return mappatura


def trova(valore: int, mappatura: List[Tuple[range, int]]) -> int:
    for intervallo, fine in mappatura:
        if valore in intervallo:
            return valore - intervallo.start + fine
    else:
        return valore


def parte_1():
    righe = leggi_righe_in_lista()

    riga_seeds = righe.pop(0).split("seeds: ")[1]
    seeds = [int(valore) for valore in riga_seeds.split()]

    righe.pop(0)

    mappature = []
    for _ in range(7):
        mappature.append(leggi_mappa(righe))

    minimo = sys.maxsize
    for corrente in seeds:
        for mappa in mappature:
            corrente = trova(corrente, mappa)
        minimo = min(minimo, corrente)

    print(f"Parte 1: {minimo}")


def parte_2():
    righe = leggi_righe_in_lista()

    riga_seeds = righe.pop(0).split("seeds: ")[1]
    seeds: List[range] = []
    indice_parte_due = 0
    riga_seeds_parte_due = riga_seeds.split()
    while indice_parte_due < len(riga_seeds_parte_due):
        inizio = int(riga_seeds_parte_due[indice_parte_due])
        lunghezza = int(riga_seeds_parte_due[indice_parte_due + 1])
        seeds.append(range(inizio, inizio + lunghezza))
        indice_parte_due += 2

    righe.pop(0)

    mappature: List[List[Tuple[range, int]]] = []
    for _ in range(7):
        mappature.append(leggi_mappa(righe))

    minimo = sys.maxsize
    for intervallo_seeds in seeds:
        intervalli = [intervallo_seeds]
        for mappatura in mappature:
            nuovi_intervalli = []
            while intervalli:
                intervallo_corrente = intervalli.pop()
                for intervallo_mappa, nuovo_inizio in mappatura:
                    nuovo_inizio_intervallo = max(intervallo_mappa.start, intervallo_corrente.start)
                    nuovo_fine_intervallo = min(intervallo_mappa.stop, intervallo_corrente.stop)

                    if range(nuovo_inizio_intervallo, nuovo_fine_intervallo):
                        offset = nuovo_inizio - intervallo_mappa.start
                        nuovo_intervallo = range(nuovo_inizio_intervallo + offset, nuovo_fine_intervallo + offset)
                        nuovi_intervalli.append(nuovo_intervallo)

                        if nuovo_inizio_intervallo > intervallo_corrente.start:
                            intervalli.append(range(intervallo_corrente.start, nuovo_inizio_intervallo))

                        if nuovo_fine_intervallo < intervallo_corrente.stop:
                            intervalli.append(range(nuovo_fine_intervallo, intervallo_corrente.stop))

                        break
                else:
                    nuovi_intervalli.append(intervallo_corrente)
            intervalli = nuovi_intervalli

        minimo = min(minimo, min([intervallo.start for intervallo in intervalli]))

    print(f"Parte 2: {minimo}")


parte_1()
parte_2()
