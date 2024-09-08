class Contato:
    def __init__(self, telefone, email):
        self.telefone = telefone
        self.email = email

    @property
    def telefone(self):
        return self._telefone

    @property
    def email(self):
        return self._email

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @email.setter
    def email(self, email):
        self._email = email
    

    def __str__(self):
        return f"Telefone: {self.telefone}, Email: {self.email}"
