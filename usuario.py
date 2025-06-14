class Usuario:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

    def exibirInformacoes(self):
        print(f'Nome: {self.nome}\nID: {self.id}')

    def exibirTipo(self):
        print()

class Professor(Usuario):

    def __init__(self, nome, id, departamento):
        super().__init__(nome, id) 
        self.departamento = departamento
    
class Aluno(Usuario):

    def __init__(self, nome, id, curso):
        super().__init__(nome, id) 
        self.curso = curso

  
