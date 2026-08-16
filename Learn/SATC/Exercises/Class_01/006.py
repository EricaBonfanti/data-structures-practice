# Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class pessoa:
    def __init__ (self, nome = "", idade = 0, peso = 0, altura = 0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade = self.idade + 1

    def engordar(self):
        self.peso += 5

    def emagrecer(self):
        self.peso -= 7

    def crescer(self):
        if self.idade < 21:
            self.altura += 0.05
            print(f"Você aumentou 5cm de tamanho. agora está com{self.altura}")
        else:
             print("Você não cresce mais, hehe!")

pessoa1 = pessoa()

pessoa1.nome = "Érica"
pessoa1.idade = 18
pessoa1.altura = 1.70
pessoa1.peso = 65

pessoa1.engordar()
pessoa1.emagrecer()
pessoa1.crescer()
pessoa1.envelhecer()

print(f"Você, {pessoa1.nome}, tem {pessoa1.idade} anos e atualmente tem {pessoa1.altura}cm de altura e está pesando {pessoa1.peso}")
