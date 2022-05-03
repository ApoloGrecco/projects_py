import requests


class SearchAdress:

    def __init__(self, cep):
        cep = str(cep)
        if self.valid_cep(cep):
            self.cep = cep
        else:
            raise ValueError("Cep inválido!!")

    def __str__(self):
        return self.format_cep()

    def valid_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    def acess_cep(self):
        url = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/")
        datas = url.json()
        return (
            datas['bairro'],
            datas['localidade'],
            datas['uf']
        )
