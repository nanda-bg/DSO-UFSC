from Empréstimo.Empréstimo import Empréstimo

class Sistema:
    def __init__(self):
        self.amigos = []
        self.livros = []
        self.emprestimos = []

    def cadastrar_amigo(self, amigo):
        self.amigos.append(amigo)

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def registrar_emprestimo(self, amigo, livro, data = None):
        emprestimo = Empréstimo(amigo, livro, data)
        self.emprestimos.append(emprestimo)

    def listar_emprestimos(self):
        return [str(emprestimo) for emprestimo in self.emprestimos]

    def livros_com_amigos(self, amigo):
        livros_com_amigo = [emprestimo._livro for emprestimo in self.emprestimos if emprestimo._amigo == amigo]
        return livros_com_amigo
