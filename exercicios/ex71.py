print('-' * 40)
print(f'{"Caixa Eletônico":^40}')
qtd_notas_50 = qtd_notas_20 = qtd_notas_10 = qtd_notas_1 = 0
print('-' * 40)
valor_saque = int(input('Digite o valor que deseja sacar:'))
if valor_saque >= 50:  # se saque maior ou igual a 50
    qtd_notas_50 = valor_saque // 50  # {qtd_notas_50} vai receber a divisão exata de {valor_saque} por 50, assim veremos quantas notas de 50 serão usadas
    valor_notas_50 = qtd_notas_50 * 50  # {valor_notas_50} vai receber {qtd_notas_50} * 50 para guardar o valor
    valor_saque -= valor_notas_50  # {valor_saque} vai ser atualizado subtraindo o {valor_notas_50}. Com o valor atualizado, vai fazer o mesmo processo com as outras notas.
if valor_saque >= 20:
    qtd_notas_20 = valor_saque // 20
    valor_notas_20 = qtd_notas_20 * 20
    valor_saque -= valor_notas_20
if valor_saque >= 10:
    qtd_notas_10 = valor_saque // 10
    valor_notas_10 = qtd_notas_10 * 10
    valor_saque -= valor_notas_10
if valor_saque >= 1:
    qtd_notas_1 = valor_saque
print(f'Total de {qtd_notas_50} cédulas de R$50')
print(f'Total de {qtd_notas_20} cédulas de R$20')
print(f'Total de {qtd_notas_10} cédulas de R$10')
print(f'Total de {qtd_notas_1} cédulas de R$1')
print('-' * 40)
print(f'{"Volte sempre ao nosso BANCO":^40}')
# dar opções de mais notas de 20, ou 10, como em um caixa de verdade
