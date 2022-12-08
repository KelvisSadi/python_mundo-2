from datetime import date
print('Serviço de alistamento - Exercito Brasileiro')
nome = str(input('Digite seu nome completo:')).strip()
nasc = int(input('Digite seu ano de nascimento para verificação:'))
sexo = int(input(' Digite [ 1 ] para sexo masculino: \n Digite [ 2 ] para sexo feminino: \n Sua opção:'))
atual = date.today().year
idade = atual - nasc
print('''Estamos verificando a sua situação de serviço militar!
.
.
.
''')
#sexo
if sexo == 2:
    print(f'Olá {nome}, o alistamento obrigatório é somente para o sexo masculino!')
    print(f'Se tiver interesse em ingressar na carreira militar brasileira siga este link: \033[1;97;40m[ALISTAMENTO FEMININO]\033[m')
elif sexo != 1 and 2:
    print('Opção invalida escolha [ 1 ] ou [ 2 ]')
#18 anos
elif idade == 18:
    print(f'Você tem 18 anos de idade, está na hora de servir seu país. ALISTE-SE NA JUNTA MILITAR MAIS PRÓXIMA!')
#menos de 18 anos
elif idade < 18:
    saldo = 18 - idade
    if saldo > 1:
        plural_singular = 'anos'
        verbo = 'faltam'
    else:
        plural_singular = 'ano'
        verbo = 'falta'
    print(f'Olá {nome.upper()} {verbo} {saldo} {plural_singular} para você se alistar no Exercito Brasileiro!')
    print(f'Seu alistamento será em {atual + saldo}!')
#mais de 18 anos
else:
    saldo = idade - 18
    if saldo > 1:
        plural_singular = 'anos'
    else:
        plural_singular = 'ano'
    print(f'Olá {nome.upper()} você ja ultrapassou {saldo} {plural_singular} do prazo de alistamento obrigatório!')
    print(f'Seu alistamento foi em {atual - saldo}')
