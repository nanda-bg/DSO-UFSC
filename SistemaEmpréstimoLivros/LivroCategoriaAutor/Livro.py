from LivroCategoriaAutor.Autor import Autor
from LivroCategoriaAutor.Categoria import Categoria

class Livro:
    def __init__(self, titulo, resumo, autor, categoria, personagem_principal):
        self.titulo = titulo
        self.resumo = resumo
        self.autor = Autor(autor)
        self.categoria = Categoria(categoria[0], categoria[1])
        self.personagem_principal = personagem_principal

    def __str__(self):
        return (f"Título: {self.titulo}, Resumo: {self.resumo}, Autor: {self.autor}, "
                f"Categoria: {self.categoria}, Personagem Principal: {self.personagem_principal}")


    @property
    def titulo(self):
        return self._titulo

    @property
    def resumo(self):
        return self._resumo

    @property
    def autor(self):
        return self._autor

    @property
    def personagem_principal(self):
        return self._personagem_principal

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @resumo.setter
    def resumo(self, resumo):
        self._resumo = resumo

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @personagem_principal.setter
    def personagem_principal(self, personagem_principal):
        self._personagem_principal = personagem_principal