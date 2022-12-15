print('Programa de Vendas')
nome_produto = nome_mais_barato = ''
qtd_mais_de_mil = gasto_total = mais_barato = 0
contador = 1
produtos = []
while True:  # while infinito n1
    print('-'*40)
    nome_produto = str(input(f'Digite o nome do {contador}º prouto:'))
    print('-'*40)
    preço_produto = float(input(f'Digite o preço do {contador}º produto [{nome_produto}] R$:'))
    produtos.append(nome_produto)  # add na lista produtos
    gasto_total += preço_produto
    if contador == 1 or preço_produto < mais_barato:  # se primeira vez ou se aparecer um mais barato
        mais_barato = preço_produto
        nome_mais_barato = nome_produto
    if preço_produto > 1000:  # se mais de mil
        qtd_mais_de_mil += 1
    print('-'*40)
    print(f'O produto {nome_produto} foi adicionado.')
    print('-'*40)
    print('Digite [S] para continuar\nDigite [N] para encerrar')
    continuar = ' '
    while continuar != 'S' and continuar != 'N':  # while continuar diferente de 's' e 'n' faça
        continuar = str(input('Sua opção:')).strip().upper()[0]
    if continuar == 'N':
        break  # break n1
    contador += 1
print('-'*40)
print(f'Os produtos selecionados foram {produtos}')
print(f'O gasto total foi de R${gasto_total:.2f}')
print(f'Ao todo {qtd_mais_de_mil} produtos custam mais de mil reais')
print(f'O produto mais barato é [{nome_mais_barato}] que custa R${mais_barato:.2f}')
print('-'*40)
print('Obrigado pro comprar em nossas lojas! Tenha um ótimo dia!')
