class Livro:
    def __init__(self, titulo, autor, isbn, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponibilidade = disponibilidade

    def emprestar(self):
        self.disponibilidade = False
        print('Livro emprestado\n')

    def devolver(self):
        self.disponibilidade = True
        print('Livro devolvido\n')
    
    def exibirInformacoes(self):
        print(f'Titulo: {self.titulo}\nAutor: {self.autor}\nISBN: {self.isbn}\nDisponibilidade: {"Disponivel" if self.disponibilidade else "Indisponivel"} ')




    
