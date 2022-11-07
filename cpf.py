class Cpf:
    def __init__(self, cpf):
        self.documento = cpf
        if self.primeira_validacao() and self.segunda_validacao() and self.terceira_validacao() and self.quarta_validacao():
            self._cpf = self.documento
        else:
            raise ValueError('CPF Inválido!!')

    def __str__(self):
        return self.formata_cpf()

    def primeira_validacao(self):
        if len(self.documento) == 11:
            return True
        else:
            return False

    def segunda_validacao(self):
        soma = 0
        for n in range(10,1,-1):
            soma += int(self.documento[10-n])*n
        resto = (soma*10)%11
        if resto == 10:
            resto = 0
        if str(resto) == self.documento[9]:
            return True
        else:
            return False

    def terceira_validacao(self):
        soma = 0
        for n in range(11,1,-1):
            soma += int(self.documento[11-n])*n
        resto = (soma*10)%11
        if resto == 10:
            resto = 0
        if str(resto) == self.documento[10]:
            return True
        else:
            return False

    def quarta_validacao(self):
        iguais = 0
        for digito in self.documento:
            if digito == self.documento[0]:
                iguais += 1
        if iguais == 11:
            return False
        else:
            return True
     
    def formata_cpf(self):
        fatia_1 = self._cpf[0:3]
        fatia_2 = self._cpf[3:6]
        fatia_3 = self._cpf[6:9]
        fatia_4 = self._cpf[9:]
        return fatia_1 + '.' + fatia_2 + '.' + fatia_3 + '-' + fatia_4
