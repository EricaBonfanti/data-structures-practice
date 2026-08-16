class Paciente:
    def __init__(self, nome="", idade=0, historicoDeConsultas=0):
        self.nome = nome
        self.idade = idade
        self.historicoDeConsultas = historicoDeConsultas

    def novaConsulta(self):
        consulta = input("Você deseja realizar uma nova consulta? (S/N) ")

        if consulta.upper() == "S":
            self.historicoDeConsultas += 1
            print("Consulta adicionada!")
        else:
            print("Você não agendou consulta.")

    def exibirConsulta(self):
        print(f"{self.nome} realizou {self.historicoDeConsultas} consultas.")


paciente1 = Paciente()
paciente1.nome = "Isabelly"
paciente1.idade = 18

paciente1.novaConsulta()
paciente1.exibirConsulta()