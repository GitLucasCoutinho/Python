# Definição da classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Instanciando objetos da classe Pessoa
pessoa1 = Pessoa("Lucas", 25)
pessoa2 = Pessoa("Maria", 30)
pessoa3 = Pessoa("João", 18)

# Chamando o método apresentar
pessoa1.apresentar()
pessoa2.apresentar()
pessoa3.apresentar()