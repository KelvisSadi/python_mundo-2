numeros = []
num_entrada = soma = quantidade = 0 #n recebe s que recebe quant que recebe zero, ou seja todos recebem zero em 1 linha
while num_entrada != 999:
    num_entrada = int(input('Para sair do programa [digite 999]\nDigite um número para adicionar a soma:'))
    if num_entrada != 999:
        numeros.append(num_entrada)
        soma += num_entrada
        quantidade += 1
print(f'os {quantidade} valores foram {numeros} e a soma deles é: {soma} ')
