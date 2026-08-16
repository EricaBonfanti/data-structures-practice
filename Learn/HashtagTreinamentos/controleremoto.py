
# caracteristica do controle (pçlargura, altura, cor)
#caracteristica:
# - cor
# - altura
# - tamanho

# atributos é o que ele faz (metodo de aumentar volume (botões))
#metodos do controle remoto:
# - passar de canal
# - mexer no volume
# - abrir a netflix

class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        #dentro do init sempre as características
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        
    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentar Canal")
        elif botao == "-":
            print("Diminuir o Canal")

# primeira intância = um objeto, um controle.
controle_remoto = ControleRemoto("preto", "10cm", "2cm", "2cm")
print(controle_remoto.cor)
# utilizou a classe ControleRemoto para ser criado.
#controle_remoto2 = ControleRemoto()
controle_remoto.passar_canal("+")