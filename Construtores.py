# Classe Pessoa com construtor
class Pessoa:
    def __init__(self, nome="Desconhecido", idade=0):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Instanciando objetos com diferentes formas de usar o construtor
p1 = Pessoa("Lucas", 25)   # passando nome e idade
p2 = Pessoa("Maria", 30)   # passando nome e idade
p3 = Pessoa()              # usando valores padrão

# Chamando o método apresentar
p1.apresentar()
p2.apresentar()
p3.apresentar()