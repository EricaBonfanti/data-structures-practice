# Implemente uma classe chamada “Livro” 
# com atributos para armazenar o título, o autor e o número de páginas do livro.
# Adicione métodos para emprestar o livro, devolvê-lo e verificar se está disponível.

class livro:
    def __init__ (self, titulo = "", autor = "", nPag = 0, qtdLivro = 0):
        self.titulo = titulo
        self.autor = autor
        self.nPag = nPag
        self.qtdLivro = qtdLivro

    def emprestarLivro(self):
        print(f"Existe {self.qtdLivro} livros disponíveis!")
        self.emprestarLivro = input("Deseja Emprestar o livro? (S / N)")
        if self.emprestarLivro.upper() == "S":
            self.qtdLivro -= 1
            print(f"Livro emprestado. Agora você possui {self.qtdLivro} livros, de {self.titulo}!") 
        else:
            print("Não emprestado.")
        
    def devolverLivro(self):
        print("="*60)
        print(f"Existe {self.qtdLivro} livros disponíveis!")
        self.devolverLivro = input("Deseja Devolver o livro? (S / N)")
        if self.devolverLivro.upper() == "S":
            self.qtdLivro += 1
            print(f"Livro devolvido. Agora você possui {self.qtdLivro} livros, de {self.titulo}!")
        else:
            print("Não devolvido.")   

    def verificarDisponibilidade(self):
        print("="*60)
        if self.qtdLivro == 0:
            print("Todos os livros já foram emprestados.")
        else:
            print (f"É possível emprestar. Existe ainda {self.qtdLivro} disponíveis do livro {self.titulo}!")


#Objeto 1
livro1 = livro()
livro1.titulo = "Amor não É Obvio"
livro1.autor = "Elayne Baeta"
livro1.nPag = 521
livro1.qtdLivro = 6

livro1.emprestarLivro()
livro1.devolverLivro()
livro1.verificarDisponibilidade()


#Objeto 2
livro2 = livro()
livro2.autor = "Colen Hoover"
livro2.titulo = "Verity"
livro2.nPag = 210
livro1.qtdLivro = 6

