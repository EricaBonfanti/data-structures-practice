# Declaração de Classe:
class Gafanhoto:
    """
    Essa classe cria um gafanhoto que é uma 
    pessoa que tem o nome e idade
    para criar uma nova pessoa, use
    variavel1 = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "vazio", idade = 0): #Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Método de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self): # Dunder Method
        return f"{self.nome} é Gafanhota e tem {self.idade} anos de idade."

    def __getstate(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

# Declaração de Objeto
g1 = Gafanhoto("isabelly", 18)
g1.aniversario()
#print(g1)

#print(g1) # Dunder Attribute
print(g1.__dict__) #Como um diiconario
print(g1.__getstate__()) #method
print(g1.__class__) #irá mostrar a classe
# Para o def __str__

# print(g1.__doc__) testar depois

g2 = Gafanhoto("Érica", 19)
g2.aniversario()
print(g2.__getstate__())