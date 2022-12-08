print('somador de números ímpares multiplos por 3, de 1 a 500')
s = 0
q = 0
for c in range(1, 501, 2):#laço c no range de 1 a 501, pulando de 2 em 2 para ficar somente números ímpares
    if c % 3 == 0:#se o resto da divisão de c por 3 for 0 faça
        s += c#s recebe ele mesmo mais c
        q += 1#q recebe ele mesmo mais 1
print(f'A soma dos {q} números ímpares multiplos de 3, no intervalo de 1 a 500, é {s}')
