import re
import math

with open('day8.in', 'r') as f:
    input_data = f.read().splitlines()

rete = {}
for line in input_data[2:]:
    nodo, sx, dx = re.match(r'(\w{3}) = \((\w{3}), (\w{3})\)', line).groups()
    rete[nodo] = (sx, dx)


def sequenza_direzioni() -> str:
    sequenza = input_data[0]
    while True:
        yield from sequenza


nodo_corr = 'AAA'
c = 0
istr = sequenza_direzioni()
while nodo_corr != 'ZZZ':
    prossima_sx, prossima_dx = rete[nodo_corr]
    nodo_corrente = prossima_sx if next(istr) == 'L' else prossima_dx
    c+= 1

print(c)

# Parte 2
cc = []
nodi_startxx = [nodo for nodo in rete.keys() if nodo.endswith('A')]
for nodo_start in nodi_startxx:
    nodo_corrente = nodo_start
    c = 0
    istr = sequenza_direzioni()
    while not nodo_corrente.endswith('Z'):
        prossima_sx, prossima_dx = rete[nodo_corr]
        nodo_corrente = prossima_sx if next(istr) == 'L' else prossima_dx
        c += 1
    cc.append(c)

# sembra che i dati di input siano progettati per consentire questo trucco
print(math.lcm(*cc))
