fila = input("Introduza os clientes da fila [cliente1, cliente2, cliente3]: \n>").split(", ")
sair = None

while sair != True:
    print("<----- MENU ----->".center(100))
    print("Atuais clientes na fila: {}".format(fila))
    print("1. Reservar mesa")
    print("2. Chamar cliente")
    print("0. Sair")
    acao = int(input(">")) 
    if acao == 1: # Reservar mesa
        cliente = input("Introduza o nome do cliente: ")
        fila.append(cliente)
        print(fila)
    elif acao == 2: # Chamar cliente
        if len(fila) != 0:
            fila.remove(fila[0])
        else:
            print("Não há clientes na fila! Use a opção 1 para adicionar clientes!")
            enter = input("Prima enter para continuar.")
    elif acao == 0:
        if len(fila) != 0:
            acao2 = input("Deseja mesmo sair? Ainda há clientes na fila! [Sim/Não]\n")
            if acao2 == "Sim":
                exit()
            elif acao2 == "Não":
                pass
        else:
            exit()
    else:
        acao = input("Valor errado! Introduza novamente: ")

