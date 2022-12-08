print('Leitura de números')
continuar = 's'
quantidade = 0
soma = 0
media = 0
while continuar == 's':
    num = int(input('Digite um número inteiro:'))
    quantidade += 1
    if quantidade == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    continuar = str(input('Quer continuar [S/N]:')).strip().lower()
media = soma / quantidade
print(f'A média de todos os valores digitados é:{media}, o maior valor é {maior} e o menor valor é {menor}')
