"""
Funções a criar:
pilha_
    pop - remove um elemento da pilha
    push - insere um elemento na pilha
    seek - devolve o último elemento da pilha sem o retirar
    count - devolve o total de elementos da pilha

fila_
    DeQueue - remove um elemento da fila
    EnQueue - insere um elemento na fila
    seek - devolve o primeiro elemento da fila
    count - devolve o total de elementos da fila

"""
lista = [1, 2, 3]

class Pilha:
    # def __init__(pilha):

    def pop(pilha):
        return(pilha.pop(-1))
    def push(pilha, elemento):
        pilha.insert(len(pilha), elemento)
        return(elemento)
    def seek(pilha):
        return(pilha[-1])
    def count(pilha):
        return("Esta pilha tem {} elementos.".format(len(pilha)))

class Fila:
    executar = None
    # def __init__(fila):
    def pop(fila):
        return(fila.pop(0))
    def push(fila, elemento):
        fila.insert(len(fila), elemento)
        return(elemento)
    def seek(fila):
        return(fila[0])
    def count(fila):
        return("Esta fila tem {} elementos.".format(len(fila)))


for i in range(4, 8):
    print(Pilha.push(lista, i))

print(lista)
