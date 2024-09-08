class Autor:
    def __init__(self, nome):
        self.nome = nome


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    

    def __str__(self):
        return self.nome
