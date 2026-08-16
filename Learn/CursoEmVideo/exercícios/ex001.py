# Declaração de Classe:
class Gafanhoto:
    def __init__(self): #Método Construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Método de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhota e tem {self.idade} anos de idade."


#Declaração de Objeto
g1 = Gafanhoto()
g1.nome = "Isabelly"
g1.idade = 18
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Érica"
g2.idade = 18
g2.aniversario()
print(g2.mensagem())