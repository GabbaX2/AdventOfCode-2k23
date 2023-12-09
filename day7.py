#parte 1

with open('day7.in', 'r') as f:
    input_data = f.read().splitlines()

def determina_tipo_mano(mano: str) -> int:
    opzioni_tipo_mano = [
        [5],             # Cinque carte uguali
        [4, 1],          # Quattro carte uguali
        [3, 2],          # Full house
        [3, 1, 1],       # Tre carte uguali
        [2, 2, 1],       # Due coppie
        [2, 1, 1, 1],    # Una coppia
        [1, 1, 1, 1, 1]  # Carta alta
    ]
    conteggi_etichette = [mano.count(carta) for carta in set(mano)]
    conteggi_etichette.sort(reverse=True)
    return opzioni_tipo_mano.index(conteggi_etichette)

def converti_carte_in_int(mano: str) -> tuple:
    etichette_ordinate = 'AKQJT98765432'
    return tuple(etichette_ordinate.index(carta) for carta in mano)

mano_giocatori = []  # tuple (ordinabili) di tipo, valori carte, e puntata
for linea in input_data:
    mano, puntata = linea.split(' ')
    mano_encoded = (
        determina_tipo_mano(mano),
        *converti_carte_in_int(mano),
        int(puntata)
    )
    mano_giocatori.append(mano_encoded)

mano_giocatori.sort(reverse=True)
vincite = sum(rango * giocatore[-1]  # rango * puntata
              for rango, giocatore in enumerate(mano_giocatori, start=1))

print(vincite)

#parte 2
with open('day7.in', 'r') as f:
    input_data = f.read().splitlines()

def determina_tipo_mano(mano: str) -> int:
    opzioni_tipo_mano = [
        [5],             # Cinque carte uguali
        [4, 1],          # Quattro carte uguali
        [3, 2],          # Full house
        [3, 1, 1],       # Tre carte uguali
        [2, 2, 1],       # Due coppie
        [2, 1, 1, 1],    # Una coppia
        [1, 1, 1, 1, 1]  # Carta alta
    ]
    conteggi_etichette = [mano.count(carta) for carta in set(mano) if carta != 'J'] \
        or [0]  # solo jolly
    conteggi_etichette.sort(reverse=True)
    conteggi_etichette[0] += mano.count('J')  # aumenta il conteggio più alto
    return opzioni_tipo_mano.index(conteggi_etichette)

def converti_carte_in_int(mano: str) -> tuple:
    etichette_ordinate = 'AKQT98765432J'
    return tuple(etichette_ordinate.index(carta) for carta in mano)

mano_giocatori = []  # tuple (ordinabili) di tipo, valori carte, e puntata
for linea in input_data:
    mano, puntata = linea.split(' ')
    mano_encoded = (
        determina_tipo_mano(mano),
        *converti_carte_in_int(mano),
        int(puntata)
    )
    mano_giocatori.append(mano_encoded)

mano_giocatori.sort(reverse=True)
vincite = sum(rango * giocatore[-1]  # rango * puntata
              for rango, giocatore in enumerate(mano_giocatori, start=1))

print(vincite)

