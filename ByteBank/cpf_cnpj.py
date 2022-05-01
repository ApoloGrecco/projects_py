from validate_docbr import CPF, CNPJ


class Document:

    @staticmethod
    def create_document(document):
        if len(document) == 11:
            return DocCpf(document)
        elif len(document) == 14:
            return DocCnpj(document)
        else:
            raise ValueError("Documento incorreto!!")


class DocCpf:
    def __init__(self, document):
        if self.valid(document):
            self.cpf = document
        else:
            raise ValueError("Cpf inválido!!")

    def __str__(self):
        return self.format()

    def valid(selfself, document):
        validator = CPF()
        return validator.validate(document)

    def format(self):
        mask = CPF()
        return mask.mask(self.cpf)


class DocCnpj:
    def __init__(self, document):
        if self.valid(document):
            self.cnpj = document
        else:
            raise ValueError("Cnpj inválido!!")

    def __str__(self):
        return self.format()

    def valid(selfself, document):
        validator = CNPJ()
        return validator.validate(document)

    def format(self):
        mask = CNPJ()
        return mask.mask(self.cnpj)
