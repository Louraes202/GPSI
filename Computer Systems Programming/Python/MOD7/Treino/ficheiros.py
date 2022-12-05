# import os
# cwd = os.getcwd()
f = open("Treino\data.txt", "r+") # abrir o ficheiro

content = f.read()
print(content)

f.write("e")
f.close() # fechar o ficheiro