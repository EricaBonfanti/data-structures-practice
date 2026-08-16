# Classe Quadrado: Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class quadrado:
    def __init__(self, tamanhoLado = 17):
        self.tamanhoLado = tamanhoLado
        
    def mudarTamanhoLado(self):
        self.tamanhoLado = 40

    def calculaAreaLado(self):
        area = self.tamanhoLado * self.tamanhoLado
        return area

quadrado1 = quadrado()
quadrado1.mudarTamanhoLado()
print(f"O tamanho dos lados alterados é: {quadrado1.tamanhoLado}, e a sua área:{quadrado1.calculaAreaLado()}")
    
