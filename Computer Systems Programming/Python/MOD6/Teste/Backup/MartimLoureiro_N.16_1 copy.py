tempos = (1,)
N = 0
stop = None
totalvoltas = []
while stop != True:
    # variáveis
        N += 1
        tempos = tuple(map(float, input("Introduza os tempos das voltas (em minutos): ").split())) # os tempos das voltas, em minutos
        if tempos != (0,):
            voltas = len(tempos) # número de voltas
            list_tempos = list(tempos) # tupla passada para lista para os métodos serem aplicados
            tempomaisrapido = min(list_tempos) # o tempo da volta mais rápida, em minutos
            voltamaisrapida = list_tempos.index(tempomaisrapido) + 1 # o número da volta mais rápida
            media = round(sum(list_tempos) / len(tempos), 1) # a média, em minutos, dos tempos de cada volta
            
            list_tempos.sort()
            totalvoltas.append(tempomaisrapido)

            print("🏁 PILOTO {} 🏁 -----------------------------------------------------------------------".format(N))
            print("-> A volta mais rápida foi de {} minutos e foi a {}.ª volta.".format(tempomaisrapido, voltamaisrapida))
            print("-> O piloto deu {} voltas e a média de tempo das voltas é {} minutos.".format(voltas, media))
            for elemento in list_tempos:
                print("{}.ª volta mais rápida de {} minutos".format(list_tempos.index(elemento) + 1, elemento), end=" | ")
            print()
            print("🏁 -------- 🏁 ----------------------------------------------------------------------")
        else:
            stop = True



totalvoltastupla = tuple(totalvoltas)
totalvoltas.sort()

contador = 0
for elemento in totalvoltas:
    contador += 1
    piloto = totalvoltastupla.index(elemento) + 1
    print("A {}.ª volta mais rápida teve o tempo de {} minutos e foi do piloto {}.".format(contador, elemento, piloto))
