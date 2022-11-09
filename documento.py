from cpf import CPF
from cnpj import CNPJ

class documento():
    @staticmethod
    def valida(doc):
        if len(doc) == 11:
            return CPF(doc)
        elif len(doc) == 14:
            return CNPJ(doc)
        else:
            raise ValueError('Quantidade de digitos inválida!!')


doc = documento.valida('00408097221')
print(doc)
