print('IBGE V2')
qtd_maiores_18 = qtd_homens_cadastrados = qtd_mulheres_menos_20 = participantes = 0
contador = 1
while True:
    idade = int(input(f'|{contador}ª Pessoa| Digite a idade:'))
    sexo = str(input(f'|{contador}ª Pessoa| Digite o sexo [M/F]:')).strip().upper()
    if sexo == 'M' or sexo == 'F':
        if idade >= 18:
            qtd_maiores_18 += 1
        if sexo == 'M':
            qtd_homens_cadastrados += 1
        if sexo == 'F' and idade < 20:
            qtd_mulheres_menos_20 += 1
        participantes += 1
        contador += 1
    else:
        print('Opção Invalida! Esolha o sexo com [M] ou [F] ')
    print('-'*40)
    print('Digite [SAIR] para sair OU [QUALQUER TECLA] para continuar')
    continuar = str(input('Sua Opção:')).strip().upper()
    if continuar == 'SAIR':
        break
print(f'Ao todo foram lidos {participantes} participantes, {qtd_homens_cadastrados} homens cadastrados e {qtd_mulheres_menos_20} mulheres com menos de 20 anos!')