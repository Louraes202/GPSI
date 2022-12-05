"""
o programa deve indicar qual o número e tempo da volta mais rápida, 
o número de voltas dadas pelo piloto e a média do tempo obtido. 
Deve também mostrar a lista completa de todas as voltas ordenadas da mais rápida para a menos rápida, 
indicando o número da volta.
"""
# 20.7 12 30 0.7

# variáveis
Npilotos = 1
# tempos = tuple(map(float, input().split()))
tempos = (20.7, 12, 30, 0.7)
voltas = len(tempos)
list_tempos = list(tempos)
tempomaisrapido = min(list_tempos)
voltamaisrapida = list_tempos.index(tempomaisrapido) + 1
media = round(sum(list_tempos) / len(tempos), 1)

list_tempos.sort()
print("PILOTO {} -----------------------------------------------------------------------".format(Npilotos))
print("-> A volta mais rápida foi de {} minutos e foi a {}.ª volta.".format(tempomaisrapido, voltamaisrapida))
print("-> O piloto deu {} voltas e a média de tempo das voltas é {} minutos.".format(voltas, media))
for elemento in list_tempos:
    print("{}.ª volta mais rápida de {} minutos".format(list_tempos.index(elemento) + 1, elemento), end=" | ")