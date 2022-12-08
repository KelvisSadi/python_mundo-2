print(f'{" Shopping Kelvis - Calculo de desconto e juros ":=^100}')
valor_produto = float(input('Digite o valor do produto: R$'))
print('''Escolha a forma de pagamento
[ 1 ] Dinheiro / Pix - À vista (10% de desconto) 
[ 2 ] Cartão         - À vista (5% de desconto)
[ 3 ] Cartão         - Parcela 2x (Sem juros)
[ 4 ] Cartão         - Parcela 3x ou mais (20% de juros)''')
cond_pagamento = int(input('Sua opção:'))
#à vista 10% desconto
if cond_pagamento == 1:
    desconto = valor_produto * 0.1
    print(f'[10% de desconto] o produto de R${valor_produto:.2f} saiu por \033[1;97;43mR${valor_produto - desconto:.2f}!!!\033[m')
#à vista cartão 5% desconto
elif cond_pagamento == 2:
    desconto = valor_produto * 0.05
    print(f'[5% de desconto] o produto de R${valor_produto:.2f} saiu por R${valor_produto - desconto:.2f}! desconto de R${desconto:.2f}!')
#cartão 2x sem juros
elif cond_pagamento == 3:
    print(f'O produto de R${valor_produto:.2f} em 2x no cartão sem juros, ficou com parcelas de R${valor_produto / 2:.2f} cada!')
#cartão 3x ou mais 20% juros
elif cond_pagamento == 4:
    juros = valor_produto * 0.2
    parcelas = int(input('Quantas parcelas?'))
    preco_parcela = (valor_produto + juros) / parcelas
    print(f'A sua compra de R${valor_produto:.2f} com 20% de juros sairá por R${valor_produto + juros:.2f}!')
    print(f'Será parcelada em {parcelas}x de R${preco_parcela :.2f}')
#opção invalida
else:
    print('Opção invalida, tente novamente!')