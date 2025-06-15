class Usuario:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

    def exibirInformacoes(self):
        print(f"Nome: {self.nome}\nID: {self.id}")
        self.exibirTipoUsuario()

    def exibirTipoUsuario(self):
        print("Tipo: Usuário Genérico")


class Professor(Usuario):

    def __init__(self, nome, id, departamento):
        super().__init__(nome, id)
        self.departamento = departamento

    def exibirTipoUsuario(self):
        print("Tipo: Professor")
        print(f"Departamento: {self.departamento}")


class Aluno(Usuario):

    def __init__(self, nome, id, curso):
        super().__init__(nome, id)
        self.curso = curso

    def exibirTipoUsuario(self):
        print("Tipo: Aluno")
        print(f"Curso: {self.curso}")
