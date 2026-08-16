# Classe Retangulo: Crie uma classe que modele um retangulo:
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro

class retangulo:
    def __init__ (self, ladoA = 0, ladoB = 0):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarValorLados(self):
        self.ladoA = 20
        self.ladoB = 40

    def retornarValorLados(self):
        return (f"Lado A: {self.ladoA} e Lado B: {self.ladoB}")

    def calcularArea(self):
        self.calcularArea = self.ladoA * self.ladoB
        print(self.calcularArea)

    def calcularPerimetro(self):
        self.calcularPerimetro = (self.ladoA * 2) + (self.ladoB * 2)
        print(self.calcularPerimetro)


retangulo1 = retangulo()
retangulo1.ladoA = 10
retangulo1.ladoB = 30

retangulo1.mudarValorLados()
retangulo1.retornarValorLados()
retangulo1.calcularArea()
retangulo1.calcularPerimetro()

print(f"Lado A: {retangulo1.ladoA} \n Lado B: {retangulo1.ladoB} \n Area calculada: {retangulo1.calcularArea} \n Perimetro calculado: {retangulo1.calcularPerimetro}")
