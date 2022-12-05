caminho = input("Introduza o caminho: ")
f = open(caminho, "r")
palavra = input("Introduza a palavra: ")
content = f.readlines()
for linha in content:
    if palavra in linha.split():
        print(linha, end="")
f.close()


