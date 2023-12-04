from collections import defaultdict

FILE = 'day3.in'

# parte 1
DIREZIONI = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [-1, -1], [1, -1], [1, 1]]

def numero_da_cifre(cifre: list[str]):
    return int(''.join(cifre))

with open(FILE) as f:
    linee = f.readlines()
    somma_numeri_parte = 0
    max_x = len(linee[0].strip())
    max_y = len(linee)

    for i in range(max_y):
        cifre = []
        adiacente = False

        for j in range(max_x):
            c = linee[i][j]

            if c.isdigit():
                cifre.append(c)

                if adiacente:
                    continue

                for dx, dy in DIREZIONI:
                    x, y = j + dx, i + dy

                    if 0 <= x < max_x and 0 <= y < max_y:
                        c = linee[y][x]

                        if not adiacente and c != '.' and not c.isdigit():
                            adiacente = True
                            break
            else:
                if adiacente:
                    somma_numeri_parte += numero_da_cifre(cifre)
                cifre = []
                adiacente = False

        if adiacente:
            somma_numeri_parte += numero_da_cifre(cifre)

    print(somma_numeri_parte)

# parte 2
with open(FILE) as f:
    linee = f.readlines()
    candidati_rapporto_ingranaggio = defaultdict(list)

    max_x = len(linee[0].strip())
    max_y = len(linee)

    for i in range(max_y):
        cifre = []
        adiacenti = []

        for j in range(max_x):
            c = linee[i][j]

            if c.isdigit():
                cifre.append(c)

                if adiacenti:
                    continue

                for dx, dy in DIREZIONI:
                    x, y = j + dx, i + dy

                    if 0 <= x < max_x and 0 <= y < max_y:
                        c = linee[y][x]

                        if len(adiacenti) == 0 and c == '*':
                            adiacenti.append((x, y))
                            break
            else:
                if len(adiacenti) > 0:
                    numero_parte = numero_da_cifre(cifre)
                    for xy in adiacenti:
                        candidati_rapporto_ingranaggio[xy].append(numero_parte)

                cifre = []
                adiacenti = []

        if len(adiacenti) > 0:
            numero_parte = numero_da_cifre(cifre)
            for xy in adiacenti:
                candidati_rapporto_ingranaggio[xy].append(numero_parte)

    print(sum(ingranaggi[0] * ingranaggi[1] for ingranaggi in candidati_rapporto_ingranaggio.values() if len(ingranaggi) == 2))