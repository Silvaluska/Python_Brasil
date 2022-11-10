from datetime import datetime

class DATA:
    def __init__(self) -> None:
        self._data = datetime.today()

    def __str__(self) -> str:
        return self.formata()

    def dia_semana(self):
        dia = ['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo']
        return dia[self._data.weekday()]

    def mes(self):
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        return meses[self._data.month - 1]

    def formata(self):
        formatado = self._data.strftime('%d/%m/%Y %H:%M')
        return formatado

    def tempo_cadastro(self):
        return datetime.today() - self._data

teste = DATA()
print(teste)
        