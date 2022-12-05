caminho = input("Introduza o caminho absoluto do ficheiro: ")

def lercont(ficheiro):
    f = open(ficheiro, "r")
    content = f.read()
    f.close()
    return(content)


print(lercont(caminho))