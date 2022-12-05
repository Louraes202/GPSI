def lercont(ficheiro):
    f = open(ficheiro, "r")
    content = f.read()
    f.close()
    return(content)

caminho = input("Introduza o caminho absoluto do ficheiro: ")
print(lercont(caminho))

