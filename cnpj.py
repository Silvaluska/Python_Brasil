class CNPJ:
    def __init__(self, cnpj):
        self.documento = cnpj
        if self.valida():
            self._cnpj = self.documento

    def valida(self):
        if len(self.documento) == 14 and self.primeiro_digito() == self.documento[12] and self.segundo_digito() == self.documento[13]:
            return True
        else:
            raise ValueError('CNPJ inválido!!')

    def primeiro_digito(self):
        parte1 = self.documento[0:4]
        parte2 = self.documento[4:12]
        soma = 0
        for i in range(5,1,-1):
            soma += int(parte1[5-i])*i
        for i in range(9,1,-1):
            soma += int(parte2[9-i])*i
        resto = soma%11
        if resto < 2:
            resto = 0
        primeiro_digito = (11-resto)
        return str(primeiro_digito)

    def segundo_digito(self):
        parte1 = self.documento[0:5]
        parte2 = self.documento[5:13]
        soma = 0
        for i in range(6,1,-1):
            soma += int(parte1[6-i])*i
        for i in range(9,1,-1):
            soma += int(parte2[9-i])*i
        resto = soma%11
        if resto < 2:
            resto = 0
        segundo_digito = (11-resto)
        return str(segundo_digito)

    def __str__(self):
        parte1 = self._cnpj[0:2]
        parte2 = self._cnpj[2:5]
        parte3 = self._cnpj[5:8]
        parte4 = self._cnpj[8:12]
        parte5 = self._cnpj[12:]
        return parte1 + '.' + parte2 + '.' + parte3 + '/' + parte4 + '-' + parte5
