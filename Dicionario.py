# Criando um dicionário para armazenar nome e idade
pessoas = {
    "Lucas": 25,
    "Maria": 30,
    "João": 18,
    "Ana": 22
}

# Exibindo o dicionário completo
print("Dicionário de pessoas:", pessoas)

# Acessando um valor pela chave
print("Idade de Maria:", pessoas["Maria"])

# Adicionando um novo par chave-valor
pessoas["Carlos"] = 40

# Alterando o valor de uma chave existente
pessoas["João"] = 19

# Percorrendo o dicionário
print("\nLista de pessoas e idades:")
for nome, idade in pessoas.items():
    print(f"{nome} -> {idade} anos")