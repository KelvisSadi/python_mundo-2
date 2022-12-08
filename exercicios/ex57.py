print('IBGE')
nome = str(input('Digite seu nome:')).strip()
sexo = str(input('Digite seu sexo [M/F]:')).lower().strip()
while sexo != 'm' and sexo != 'f':#enquanto sexo for diferente de M e F faça
    sexo = str(input('Digite novamente seu sexo! escolha entre --> [M/F]')).lower()
print(f'{nome}, você concluiu nossa pesquisa!')
