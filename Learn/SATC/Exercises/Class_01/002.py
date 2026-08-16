# Crie uma classe chamada Aluno() com os seguintes atributos:
# Nome, Nota 1, Nota 2.

# Crie os seguintes métodos:
# Calcular média, retornando a média aritmética entre as notas.
# Mostrar dados, que somente imprime o valor de todos os atributos.
# Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior ou igual a 6.0, o aluno está aprovado).


class aluno:
    def __init__(self):
        self.nome = ""
        self.nota1 = 0
        self.nota2 = 0

    def calcularMedia(self):
        self.media = self.nota1 + self.nota2 / 2

    def mostrarDados(self):
        print(f"Os dados são: {self.nome}, {self.nota1},{self.nota2}")

    def resultado(self):
        if self.media >= 6:
            print("O aluno está aprovado!")
        else:
            print("O aluno está reprovado.")

aluno1 = aluno()
aluno1.nome = "Érica"
aluno1.nota1 = 6
aluno1.nota2 = 9
aluno1.calcularMedia()
aluno1.mostrarDados()
aluno1.resultado()