import requests

class BuscarEndereço:
    def __init__(self, cep) -> None:
        self.cep = cep
        if self.valida():
            self._cep = self.cep
        else:
            raise ValueError('Cep inválido!!')

    def __str__(self) -> str:
        return self.formata()

    def valida(self):
        if len(self.cep) == 8:
            return True
        else:
            return False

    def acessaAPI(self):
        json = requests.get('https://viacep.com.br/ws/'+self._cep+'/json/')
        return json.json()

    def formata(self):
        endereco = self.acessaAPI()
        return f'{endereco["bairro"]}\n{endereco["localidade"]}\n{endereco["uf"]}'

teste = BuscarEndereço('66093040')
print(teste)