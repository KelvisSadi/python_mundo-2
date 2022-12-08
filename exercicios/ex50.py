print('Somador de números pares: 6 inteiros')
soma = 0
pares = []#lista
for leitor in range(6):#laço leitor no range de 6 vezes
    num = int(input('Digite um número inteiro:'))
    if num % 2 == 0:#se o resto de num dividido por 2 for igual zero faça
        soma += num#soma recebe ele mais num
        pares.append(num)#adiciona o num a lista pares
print(f'Os pares são {pares} e a soma de todos números pares é de: {soma}')
