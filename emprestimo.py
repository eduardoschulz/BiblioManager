from livro import Livro
from usuario import Usuario

class Emprestimo:

    def __init__(self, livro:Livro, usuario:Usuario, dtEmprestimo, dtDevolucao):
        self.livro = livro
        self.usuario = usuario
        self.dtDevolucao = dtDevolucao
        self.dtEmprestimo = dtEmprestimo
        print('Livro emprestado com sucesso\n')
    
    def exibirResumo(self):
        print(f'''Resumo do Empréstimo:
Livro: {self.livro.titulo}
Usuário: {self.usuario.nome}
Data do Empréstimo: {self.dtEmprestimo}
Data de Devolução: {self.dtDevolucao}
        ''')
