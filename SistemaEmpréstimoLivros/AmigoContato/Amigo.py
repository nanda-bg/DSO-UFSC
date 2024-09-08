from AmigoContato.Contato import Contato

class Amigo:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.contato = Contato(telefone, email)


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


    def __str__(self):
        return f"Nome: {self.nome}, {self.contato}"