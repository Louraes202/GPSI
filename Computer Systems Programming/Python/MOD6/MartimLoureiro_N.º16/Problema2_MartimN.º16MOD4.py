# Dados previamente declarados, podendo ser alterados pelos professores para testes.
# Mesmo com os dados já declarados, o programa está pronto para todos os valores.
email = "navarro@esenviseu.net"
password = "NavarroViseu2022"

# restrição
if email == "":
    exit()


letras = "abcdefghijklmnopqrstuvwxyz"
numeros = "1234567890"

# get utilizador
utilizador = ""
for c in email:
    if c == "@":
        break
    utilizador += c

# verificações de segurança
if len(password) > 8: # tem de ter mais de 8 caracteres
    maisqueoito = True
else:
    maisqueoito = False

for i in range(len(letras)): # tem de ter letras
    if letras[i] in password:
        temletras = True
    else:
        temletras = False

for i in range(len(numeros)): # tem de ter numeros
    if numeros[i] in password:
        temnumeros = True
    else:
        temnumeros = False

passwordlow = password.lower() # não pode ter o utilizador na password
if utilizador in passwordlow:
    passsemnome = False
else:
    passsemnome = True

if maisqueoito and temletras and temnumeros and passsemnome:
    final = "Segura"
else:
    final = "Não Segura"

print(final)