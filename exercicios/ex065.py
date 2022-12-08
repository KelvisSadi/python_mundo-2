print('Leitura de números')
continuar = 's'
quantidade = soma = media = 0#todos recebem zero em uma linha de código
while continuar in 'Ss': #enquanto {continuar} tiver 'Ss' maiúsculo ou minúsculo faça o bloco
    num = int(input('Digite um número inteiro:'))
    quantidade += 1
    if quantidade == 1:#se for a primeira vez rodando o looping {maior} e {menor} vao receber o {num}
        maior = menor = num
    if num > maior:#se {num} maior que {maior} faça
        maior = num
    if num < menor:#se {num} menor que {menor} faça
        menor = num
    soma += num#{soma} vai somar {num}
    continuar = str(input('Quer continuar? [S/N]:')).strip()
media = soma / quantidade#{media} vai dividir {soma} pela {quantidade}
print(f'A média dos {quantidade} valores digitados é: {media}\nO maior valor é {maior}\nO menor valor é {menor}')
