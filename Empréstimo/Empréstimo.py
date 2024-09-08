from datetime import datetime

class Empréstimo:
    def __init__(self, amigo, livro, data_emprestimo=None):
        self._amigo = amigo
        self._livro = livro
        self._data_emprestimo = data_emprestimo if data_emprestimo else datetime.now().strftime("%d/%m/%Y")

    @property
    def amigo(self):
        return self._amigo

    @property
    def livro(self):
        return self._livro

    @property
    def data_emprestimo(self):
        return self._data_emprestimo

    @amigo.setter
    def amigo(self, amigo):
        self._amigo = amigo

    @livro.setter
    def livro(self, livro):
        self._livro = livro

    @data_emprestimo.setter
    def data_emprestimo(self, data_emprestimo):
        self._data_emprestimo = data_emprestimo

    def __str__(self):
        return f"Empréstimo: O livro '{self._livro.titulo}' foi emprestado para {self._amigo.nome} em {self._data_emprestimo}"
