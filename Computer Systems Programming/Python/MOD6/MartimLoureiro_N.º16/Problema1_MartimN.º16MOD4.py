# Dados previamente declarados, podendo ser alterados pelos professores para testes.
# Mesmo com os dados já declarados, o programa está pronto para todos os valores.
local = ["Viseu", "Porto", "Viseu", "Faro", "Viseu"]
golos = [4, 5, 4, 7, 1]

# restrição
for i in range(len(golos)):
    if int(golos[i]) < 0:
        exit()

# máximo de golos
maximo = max(golos)


# jornada em que se marcou mais golos (havendo caso empate)
maior = 0
for i in range(len(golos)):
    if golos[i] > maior:
        maior = golos[i]
        jornada = i + 1
    if golos[i] == maior:
        maior = golos[i]
        jornada = i + 1



# percentagem de jogos disputados em Viseu
casa = 0
totaljogos = len(golos)
for i in range(len(local)):
    if "Viseu" == local[i]:
        casa += 1
percentagem = "{0:.0f}".format((casa * 100) / totaljogos)



# total de golos
golos_total = 0
for i in range(len(golos)):
    golos_total += int(golos[i])


# output

print("O record de golos num jogo foi de {} golos, obtido na {}ª jornada. {}% dos jogos da temporada foram em casa. A equipa marcou {} golos na totalidade.".format(maximo, jornada, percentagem, golos_total))