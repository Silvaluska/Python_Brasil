import re

class TELEFONE:
    def __init__(self, telefone):
        if self.valida(telefone):
            self._tel = telefone
        else:
            raise ValueError('Telefone incorreto!!')

    def __str__(self):
        return self.formata()

    def valida(self, telefone):
        padrao = '(\d{2,3})?(\d{2})?(\d{4,5})(\d{4})'
        self._resposta = re.findall(padrao, telefone)
        if self._resposta:
            return True
        else:
            return False

    def formata(self):
        if self._resposta[0][0] == '':
            if self._resposta[0][1] == '':
                return self._resposta[0][2] + '-' + self._resposta[0][3]
            else:
                return '(' + self._resposta[0][1] + ') ' + self._resposta[0][2] + '-' + self._resposta[0][3]
        else:
            return '+' + self._resposta[0][0] + ' (' + self._resposta[0][1] + ') ' + self._resposta[0][2] + '-' + self._resposta[0][3]

numero = TELEFONE('05591983093760')
print(numero)