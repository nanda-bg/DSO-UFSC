class Categoria:
    def __init__(self, genero, faixa_etaria):
        self.genero = genero
        self.faixa_etaria = faixa_etaria


    @property
    def genero(self):
        return self._genero

    @property
    def faixa_etaria(self):
        return self._faixa_etaria

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @faixa_etaria.setter
    def faixa_etaria(self, faixa_etaria):
        self._faixa_etaria = faixa_etaria


    def __str__(self):
        return f"Gênero: {self.genero}, Faixa Etária: {self.faixa_etaria}"
