#3	Classe Bola: Crie uma classe que modele uma bola:
#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor

class bola:
    def __init__(self):
        self.cor = ""
        self.circuferencia = 0
        self.material = ""

    def trocaCor(self):
        self.cor = "rosa"

    def mostraCor(self):
        print(self.cor)

    def restoDados(self):
        print(f"A circuferência da bola é:{self.circuferencia}, Utilizando o material: {self.material}")


bola1 = bola()
bola1.cor = "Preto"
bola1.circuferencia = 18
bola1.material = "plástico"
bola1.trocaCor()
bola1.mostraCor()

# Demostrando os dados para ver se funcionou:
bola1.restoDados()