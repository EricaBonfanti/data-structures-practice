# Vamos criar uma classe para Clientes da Netflix

#Criando classe
class Cliente():
    def __init__(self, nome, email, plano):

        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception ("Plano inválido")
        self.plano = plano

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano inválido")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Ver filme {filme}")
        elif self.plano == "premium":
            print(f"Ver filme {filme}")
        elif self.plano == "basic" and plano_filme == "premium":
            print ("Faça upgrade para premium para ver este filme")
        else:
            print("Plano inválido.")
            cliente.ver_filme("Harry Potter", "premium")




#Utilizando classe
cliente = Cliente("Isa", "isa@gmail.com", "basic")
print(cliente.plano)

#no botão upgrade
cliente.mudar_plano("Premium")
print(cliente.plano)