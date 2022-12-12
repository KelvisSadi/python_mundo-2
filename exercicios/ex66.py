print('Leitor')
n = c = s = 0
digitados = []
print('Para sair Digite [999]')
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    c += 1
    s += n
    digitados.append(n)
print(f'Você digitou {c} números, que são {digitados} e a soma deles é igual a: {s}')