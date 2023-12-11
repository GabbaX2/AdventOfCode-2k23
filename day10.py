dane = open("day10.in", "r").read().splitlines()

def znajdzStart(dane):
    for x in range(len(dane)):
        for y in range(len(dane[0])):
            if dane[x][y] == "S":
                return (x, y)

start = znajdzStart(dane)

góra, dół, lewo, prawo = (-1, 0), (1, 0), (0, -1), (0, 1)

kafelki = {
    "S": [góra, dół, lewo, prawo],
    "|": [góra, dół],
    "-": [lewo, prawo],
    "L": [góra, prawo],
    "J": [góra, lewo],
    "7": [dół, lewo],
    "F": [dół, prawo],
    ".": []
}

def pętla(dane, start, kierunek):
    acc = 0
    x, y = start
    odwiedzone = set()
    while acc == 0 or (x, y) != start:
        odwiedzone.add((x, y))
        dx, dy = kierunek
        x += dx
        y += dy
        if not (0 <= x < len(dane) and 0 <= y < len(dane[0])):
            return None
        dx *= -1
        dy *= -1
        kierunekKafelka = kafelki[dane[x][y]]
        if (dx, dy) not in kierunekKafelka:
            return None
        for następnyKierunek in kierunekKafelka:
            if następnyKierunek != (dx, dy):
                kierunek = następnyKierunek
        acc += 1
    return acc, odwiedzone

dobryWynik = None
S = []
for kierunek in góra, dół, lewo, prawo:
    wynik = pętla(dane, start, kierunek)
    if wynik is not None:
        dobryWynik = wynik
        S.append(kierunek)

print(dobryWynik[0] // 2)

odwiedzone = dobryWynik[1]
kafelki["S"] = S

ręka = None
acc = 0
for x in range(len(dane)):
    wewnątrz = False
    for y in range(len(dane[0])):
        if (x, y) in odwiedzone:
            kierunekKafelka = kafelki[dane[x][y]]
            if lewo in kierunekKafelka and prawo in kierunekKafelka:
                continue
            wewnątrz = not wewnątrz
            if góra in kierunekKafelka and dół in kierunekKafelka:
                continue
            kierunekRęki = None
            for kierunek in kierunekKafelka:
                if kierunek != lewo and kierunek != prawo:
                    kierunekRęki = kierunek
            if ręka == None:
                ręka = kierunekRęki
            else:
                if kierunekRęki != ręka:
                    wewnątrz = not wewnątrz
                ręka = None
        else:
            if wewnątrz:
                acc += 1
print(acc)
