# fila = input("Introduza os clientes da fila: ").split()
fila = ["Martim", "António", "Rebeca", "Carlos"]

while len(fila) != 0:
    print("<----- MENU ----->".center(100))
    print("Atuais clientes na fila: {}".format(fila))
    print("1. Reservar mesa")
    print("2. Chamar cliente")
    acao = int(input(">")) 
    if acao == 1: # Reservar mesa
        cliente = input("Introduza o nome do cliente: ")
        fila.append(cliente)
        print(fila)
    elif acao == 2: # Chamar cliente
        fila.remove(fila[0])
    else:
        acao = input("Valor errado! Introduza novamente: ")

