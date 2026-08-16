# Escreva um método para a classe ContaCorrente() vista em aula,
# que permita a transferência de um valor de uma conta para outra.
# O método deve receber como parâmetro o valor a ser transferido e a conta destino.

class ContaConrrente:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.saldo + self.limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.pode_sacar(valor):
            self.saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    # MÉTODO PEDIDO PELO PROFESSOR
    def transfere(self, valor, conta_destino):
        if self.pode_sacar(valor):
            self.saca(valor)
            conta_destino.deposita(valor)
        else:
            print("Transferência não realizada.")

    def get_saldo(self):
        return self.saldo

    def get_titular(self):
        return self.titular

    def get_limite(self):
        return self.limite

#Criando primeiro objeto - criando contacorrente - é uma instância da classe e está executando constutor
c1 = ContaConrrente(2106, "Isabelly", 1000, 5000)
c2 = ContaConrrente(2107, "Érica", 500, 3000)

c1.transfere(40, c2)

c1.extrato()
c2.extrato()