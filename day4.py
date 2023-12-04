with open('day4.in', 'r') as dati:
    dati = [linea.strip() for linea in dati.readlines()]
    output = 0
    conteggio_copie = [0] * (len(dati) + 1)

    for linea in dati:

        # 2 parti
        linea = linea.split(':')
        id_carta = int(linea[0].split()[-1])
        linea = linea[1]

        conteggio_copie[id_carta] += 1

        linea = linea.split('|')
        numeri_vincenti = [int(num) for num in linea[0].split()]

        numeri = [int(num) for num in linea[1].split()]

        esponente = 0
        punti_correnti = 0

        for num in numeri:
            if num in numeri_vincenti:
                punti_correnti = 2 ** esponente
                esponente += 1

        if punti_correnti > 0:
            for idx in range(id_carta + 1, id_carta + esponente + 1):
                conteggio_copie[idx] += 1 * conteggio_copie[id_carta]

        output += punti_correnti

    print(output)
    print(sum(conteggio_copie))


