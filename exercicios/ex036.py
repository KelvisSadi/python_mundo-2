#ex036
print('Emprestimo Bancário - Banco XXXX')
valor_casa = float(input('Digite o valor da casa que deseja comprar: R$'))
salario = float(input('Digite o valor de seu salário: R$'))
tempo = float(input('Digite em quantos anos deseja quitar a divida:'))
prestacao_mensal = (valor_casa / tempo) / 12
aprovado = prestacao_mensal <= (salario / 100 * 30)
if aprovado:
    print('Olá o Banco XXXX informa! - seu pedido de emprestimo foi APROVADO!')
    print(f'Sua prestação mensal é de R${prestacao_mensal:.2f}')
else:
    print('Olá o Banco XXXX informa! - seu pedido de emprestimo foi NEGADO!')
    print(f'A prestação de R${prestacao_mensal:.2f} ultrapassou o limite de 30% de seu salário que é R${salario * 0.3:.2f}')
