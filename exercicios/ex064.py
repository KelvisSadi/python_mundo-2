numeros = []
num_entrada = 0
soma = 0
quantidade = 0
while num_entrada != 999:
    num_entrada = int(input('Para sair do programa digite 999\nDigite um número para adicionar a soma:'))
    if num_entrada != 999:
        numeros.append(num_entrada)
        soma += num_entrada
        quantidade += 1
print(f'os {quantidade} valores foram {numeros} e a soma deles é: {soma} ')
