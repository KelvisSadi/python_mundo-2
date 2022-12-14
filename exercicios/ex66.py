print('Leitor')
num = cont = soma = 0
digitados = []
print('Para sair Digite [999]')
while True:  # while infinito n1
    num = int(input('Digite um número:'))
    if num == 999:
        break  # break n1
    cont += 1
    soma += num
    digitados.append(num)
print(f'Você digitou {cont} valores, que são {digitados} e a soma deles é igual a: {soma}')
