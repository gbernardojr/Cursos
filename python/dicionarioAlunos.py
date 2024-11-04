# Criação de um dicionário simples com informações de alunos
alunos = {
    "João": {"idade": 20, "curso": "Engenharia"},
    "Maria": {"idade": 22, "curso": "Medicina"},
    "Pedro": {"idade": 19, "curso": "Arquitetura"}
}

# Acessando dados de um aluno específico
print("Dados de João:", alunos["João"])

# Adicionando um novo aluno ao dicionário
alunos["Ana"] = {"idade": 21, "curso": "Direito"}
print("\nDicionário após adicionar Ana:")
print(alunos)

# Atualizando dados de um aluno existente
alunos["Maria"]["idade"] = 23
print("\nDicionário após atualizar idade de Maria:")
print(alunos)

# Removendo um aluno do dicionário
del alunos["Pedro"]
print("\nDicionário após remover Pedro:")
print(alunos)

# Iterando sobre os alunos e exibindo suas informações
print("\nLista de alunos e seus dados:")
for nome, dados in alunos.items():
    print(f"Aluno: {nome}, Idade: {dados['idade']}, Curso: {dados['curso']}")

# Verificando se um aluno está no dicionário
aluno_procurado = "Ana"
if aluno_procurado in alunos:
    print(f"\n{aluno_procurado} está no dicionário.")
else:
    print(f"\n{aluno_procurado} não está no dicionário.")

# Obtendo todas as chaves e valores
print("\nNomes dos alunos cadastrados:", list(alunos.keys()))
print("Dados dos alunos:", list(alunos.values()))
