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
lista = [1, 2, 3, 4]

class Pilha:
    def __init__(lista):
        pass
    def pop(pilha):
        return(pilha.pop(-1))
    def push(pilha, elemento):
        pilha.insert(len(pilha), elemento)
        return(elemento)
    def seek(pilha):
        return(pilha[-1])
    def count(pilha):
        return("Esta pilha tem {} elementos.".format(len(pilha)))
    def stackup(pilha, stack):
        for i in range(pilha[-1]+1, stack+1):
            Pilha.push(pilha, i)
        return(pilha)


class Fila:
    def __init__(fila):
        pass
    def pop(fila):
        return(fila.pop(0))
    def push(fila, elemento):
        fila.insert(len(fila), elemento)
        return(elemento)
    def seek(fila):
        return(fila[0])
    def count(fila):
        return("Esta fila tem {} elementos.".format(len(fila)))
    def stackup(fila, stack):
        for i in range(fila[-1]+1, stack+1):
            Fila.push(fila, i)
        return(fila)


