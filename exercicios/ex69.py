print('IBGE V2')
qtd_maiores_18 = qtd_homens_cadastrados = qtd_mulheres_menos_20 = participantes = 0
sexo = 'a'
continuar = 's'
contador = 1
while True:  # while infinito n1
    print('-' * 40)
    idade = int(input(f'|{contador}ª Pessoa| Digite a idade:'))
    while True:  # while infinito n2
        sexo = str(input(f'|{contador}ª Pessoa| Digite o sexo [M/F]:')).strip().upper()[0]
        if sexo == 'M' or sexo == 'F':
            break  # break n2
    if idade >= 18:
        qtd_maiores_18 += 1
    if sexo == 'M':
        qtd_homens_cadastrados += 1
    if sexo == 'F' and idade < 20:
        qtd_mulheres_menos_20 += 1
    participantes += 1
    contador += 1
    print('-'*40)
    while True:  # while infinito n3
        print('Digite [C] para continuar\nDigite [S] para sair')
        continuar = str(input('Sua Opção:')).strip().upper()[0]
        if continuar == 'C' or continuar == 'S':
            break  # break n3
    if continuar == 'S':
        break  # break n1
print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'Total de {participantes} participantes!')
print(f'Total de {qtd_homens_cadastrados} homens cadastrados!')
print(f'Total de {qtd_mulheres_menos_20} mulheres com menos de 20 anos!')
print(f'{qtd_maiores_18} pessoas com mais de 18 anos!')
