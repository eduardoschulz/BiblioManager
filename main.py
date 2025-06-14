from livro import Livro
from usuario import Usuario, Professor, Aluno
from emprestimo import Emprestimo




l1 = Livro("livro bom", "sla", 12, True)
l1.exibirInformacoes()

u = Professor("Nome", 1, "TI")

e = Emprestimo(l1, u, "1", "12")

e.exibirResumo()


