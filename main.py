from cnpj import CNPJ
cnpj = CNPJ('45038662000199')
print(cnpj.primeiro_digito() == cnpj.documento[12])
print(cnpj.segundo_digito())
print(cnpj)

