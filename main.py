from livro import Livro
from usuario import Professor, Aluno
from emprestimo import Emprestimo

#lista para guardas os todos os livros
livros = []
#lista de emprestimos
emprestimos = []
#lista de alunos 
alunos = []
#lista de professores
professores = []

def cadastroLivro():
    print('Cadastro de Livro\n')
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    disponibilidade = True

    return Livro(titulo, autor, isbn, disponibilidade)


def cadastroUsuario():
    print("Cadastro de Usuário\n(1) - Aluno\n(2) - Professor")
    tipo = input("Escolha o tipo: ")
    nome = input("Nome: ")
    id = input("ID: ")

    if tipo == "1":
        curso = input("Curso: ")
        aluno = Aluno(nome, id, curso)
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!\n")
    elif tipo == "2":
        depto = input("Departamento: ")
        prof = Professor(nome, id, depto)
        professores.append(prof)
        print("Professor cadastrado com sucesso!\n")
    else:
        print("Tipo inválido.")


def emprestarLivro():
    if not livros:
        print("Nenhum livro disponível.\n")
        return
    print("Lista de livros disponíveis:")
    for i, livro in enumerate(livros):
        print(f"({i}) - {livro.titulo} - {'Disponível' if livro.disponibilidade else 'Indisponível'}")

    try:
        indice_livro = int(input("Escolha o número do livro: "))
        livro = livros[indice_livro]
    except:
        print("Escolha inválida.")
        return

    if not livro.disponibilidade:
        print("Livro indisponível.\n")
        return

    print("Lista de usuários:")
    todos = alunos + professores
    for i, usuario in enumerate(todos):
        print(f"({i}) - {usuario.nome}")

    try:
        indice_usuario = int(input("Escolha o número do usuário: "))
        usuario = todos[indice_usuario]
    except:
        print("Escolha inválida.")
        return

    dt_emprestimo = input("Data de empréstimo: ")
    dt_devolucao = input("Data de devolução: ")
    livro.emprestar()
    emprestimo = Emprestimo(livro, usuario, dt_emprestimo, dt_devolucao)
    emprestimos.append(emprestimo)


def exibirDados():
    print("Livros:\n")
    for livro in livros:
        livro.exibirInformacoes()

    print("Alunos:\n")
    for aluno in alunos:
        aluno.exibirInformacoes()

    print("Professores:\n")
    for prof in professores:
        prof.exibirInformacoes()

    print("Empréstimos:\n")
    for emp in emprestimos:
        emp.exibirResumo()


def devolverLivro():
    print("Livros emprestados:")
    emprestados = [e for e in emprestimos if not e.livro.disponibilidade is True]

    if not emprestados:
        print("Nenhum livro emprestado.\n")
        return

    for i, e in enumerate(emprestados):
        print(f"({i}) - {e.livro.titulo} para {e.usuario.nome}")

    try:
        indice = int(input("Escolha o número do empréstimo: "))
        emprestimo = emprestados[indice]
        emprestimo.livro.devolver()
        print("Livro devolvido com sucesso!\n")
    except:
        print("Escolha inválida.")


def parsedoinput(valor):
    match valor:
        case 1:
            livros.append(cadastroLivro())
            print("Livro cadastrado com sucesso!\n")
        case 2:
            cadastroUsuario()
        case 3:
            emprestarLivro()
        case 4:
            exibirDados()
        case 5:
            devolverLivro()
        case 6:
            exit(0)
        case _:
            print("Opção inválida.")
def printOpcoes():
    print("""Opções:
(1) - Cadastro de Livro
(2) - Cadastro de Aluno ou Professor
(3) - Empréstimo
(4) - Exibir Dados
(5) - Devolver Livro
(6) - Sair
          """)

while True:
    printOpcoes()
    recv = input()
    try:
        num = int(recv)
        parsedoinput(num)
    except ValueError:
        print('Digite um número válido')


