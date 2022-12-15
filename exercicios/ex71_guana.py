print('caixa eletrônico - jeito guanabara')
valor_saque = int(input('Digite o valor que deseja sacar: R$'))
total = valor_saque
cedula = 50
tot_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        tot_cedula += 1
    else:
        if tot_cedula > 0:
            print(f'Total de {tot_cedula} cédulas de R${cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        tot_cedula = 0  # zera o total de cedulas toda vez que muda a cedula
        if total == 0:
            break
