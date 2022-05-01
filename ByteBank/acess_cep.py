

class SearchAdress:

    def __init__(self, cep):
        cep = str(cep)
        if self.valid_cep(cep):
            self.cep = cep
        else:
            raise ValueError("Cep inválido!!")

    def __str__(self):
        return self.format_cep()

    def valid_cep (self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"
