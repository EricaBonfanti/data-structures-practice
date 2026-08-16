class ContaCorrente:

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
        if(self.pode_sacar(valor)):
            self.saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    
    def saldo(self):
        return self.saldo

    
    def get_titular(self):
        return self.titular

    
    def limite(self):
        return self.limite

    
    def limite(self, limite):
        self.limite = limite

#Criando primeiro objeto - criando contacorrente - é uma instância da classe e está executando constutor

conta1 = ContaCorrente(2025, "Érica", 2100, 31000)
conta1.extrato()

conta1.deposita(200)
conta1.extrato()

conta1.saca(40)
conta1.extrato()


conta2 = ContaCorrente(2106, "Isabelly", 1500, 20000)
conta2.extrato()

conta2.deposita(100)
conta2.extrato()

conta2.saca(20)
conta2.extrato()