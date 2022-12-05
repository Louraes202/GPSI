# Pretende-se desenvolver uma aplicação para facilitar a gestão de uma instituição de ensino.  
# A aplicação deverá guardar as disciplina em funcionamento. 
# Deverá também gerir os nomes dos alunos e, para cada aluno, 
# a lista das disciplinas em que este se encontra inscrito. 
# Esta informação deverá constituir um dicionário (nome do aluno : lista de disciplinas inscritas).
def menu(escola):
    print("Menu da escola {}".format(escola).center(100))
    print("[1] Mostrar as disciplinas")
    print("[2] Inscrever um aluno em determinada disciplina")
    acao = input("Introduza a ação que quer realizar: ")
    while acao != "1" and acao != "2":
        acao = input("Erro. Introduza o valor novamente: ")
    return(acao)
disccont = open("Exercícios/disciplinas.txt", "r", encoding="utf-8")
alunoscont = open("Exercícios/alunos.txt", "r", encoding="utf-8")

disciplinas = disccont.readlines()
alunos = alunoscont.readlines()

print(disciplinas, alunos)

acao = menu("Escola Secundária Emídio Navarro")

# if acao == "1":
    