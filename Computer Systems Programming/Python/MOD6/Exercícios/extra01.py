def menu(nomeloja):
    # menu visual
    print("✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪".center(100))
    print(nomeloja.center(100))
    print("✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪".center(100))
    # opções
    print("1 - Introduzir o cõdigo postal ou o nome da cidade:\n2 - Ordenar por cidade com mais compras\n3 - Mostrar o período do dia com mais volume de compra")
    resp = input(">")
    return(resp)

compras = [ # lista de dicionários literal
    {"Código-Postal": "3500-601", "Valor-Total": 20, "Hora": "12:40", "Dia": "30/07/2022"},
    {"Código-Postal": "4000-177", "Valor-Total": 300, "Hora": "21:00", "Dia": "17/12/2022"},
    {"Código-Postal": "0000-000", "Valor-Total": 20, "Hora": "07:30", "Dia": "02/04/2022"},
    {"Código-Postal": "0000-177", "Valor-Total": 300, "Hora": "02:39", "Dia": "03/01/2022"}
]

portalcodigos = { # base de dados CIDADE-CÓDIGO
    "Viseu": "3500:3515",
    "Porto": "4000:4825",
    "Lisboa": "1000:2795"
}

codigospostais = [] # lista para armazenar os códigos postais
for i in range(len(compras)): # ciclo para armazenar todos os códigos postais
    dictio = compras[i]
    codigospostais.append(dictio.get("Código-Postal", 0))

acao = menu("Loja do Martim")

while acao != "0" and acao != "1" and acao != "2" and acao != "3": # proteção contra ações inválidas
    acao = input("Ação inválida! Introduza a ação novamente: ")

if acao == "0":
    exit()
elif acao == "1": # 1: "Introduzir o cõdigo postal ou o nome da cidade"
    input1 = input("Introduza o código postal ou o nome da cidade: ")
    if input1.isalpha():
        print("Cidade")
    else:
        print("Cõdigo")
elif acao == "2": # 2: "Ordenar por cidade com mais compras"
    print(2)
elif acao == "3": # 3: "Mostrar o período do dia com mais volume de compra"
    print(3)