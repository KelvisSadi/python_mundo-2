print('-'*40)
print(f'{"Caixa Eletônico":^40}')
notas_50 = notas_20 = notas_10 = notas_1 = 0
print('-'*40)
valor_saque = int(input('Digite o valor que deseja sacar:'))
if valor_saque >= 50:
    notas_50 = valor_saque // 50
    valor_notas_50 = notas_50 * 50
    valor_saque -= valor_notas_50
if valor_saque >= 20:
    notas_20 = valor_saque // 20
    valor_notas_20 = notas_20 * 20
    valor_saque -= valor_notas_20
if valor_saque >= 10:
    notas_10 = valor_saque // 10
    valor_notas_10 = notas_10 * 10
    valor_saque -= valor_notas_10
if valor_saque >= 1:
    notas_1 = valor_saque
print(f'Total de {notas_50} cédulas de R$50')
print(f'Total de {notas_20} cédulas de R$20')
print(f'Total de {notas_10} cédulas de R$10')
print(f'Total de {notas_1} cédulas de R$1')
print('-'*40)
print(f'{"Volte sempre ao nosso BANCO":^40}')
#dar opções de mais notas de 20, ou 10, como em um caixa de verdade