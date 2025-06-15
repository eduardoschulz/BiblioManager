# BiblioManager 📚
## Atividade do Grau B [GB1] - Paradigmas de Programação

## Autores: 
- Eduardo Schulz
- Arthur Wild


## Estrutura de Classes

- **Livro**
  - Atributos: título, autor, ISBN, disponibilidade
  - Métodos: `emprestar()`, `devolver()`, `exibirInformacoes()`

- **Usuario** (classe base)
  - Atributos: nome, ID
  - Método: `exibirTipoUsuario()`

- **Aluno** e **Professor**
  - Aluno: possui curso
  - Professor: possui departamento
  - Ambos sobrescrevem `exibirTipoUsuario()`

- **Emprestimo**
  - Atributos: livro, usuário, data de empréstimo, data de devolução
  - Método: `exibirResumo()`

## Como Executar

1. Tenha o Python 314 instalado.
2. Execute o arquivo principal:

```bash
python main.py
```
