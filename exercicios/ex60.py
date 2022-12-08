print('Fatorial')
n1 = int(input('Digite um valor:'))#primeiro valor
multi = n1#multi recebe {n1}
print(f'{n1}! = {n1}', end='')#vai printar o começo da operação
while n1 > 1:#enquanto n1 for maior que 1 faça, vai parar no 2
    n1 -= 1#tira 1 de {n1}
    multi *= n1#vai multiplicar {n1} com o que tem em multi, obs: foi salvo {n1} em multi no começo e cada vez que entra no while subtrai 1 de {n1} e multiplica aqui ex: 5x4x3x2x1 = 120
    print(f'x{n1}', end='')
print(f' = {multi}')

#fatorial com for

print('Fatorial com For')
n2 = int(input('Digite um valor'))
multi2 = n2
print(f'{n2}! = {n2}', end='')
for f in range(n2, 1, -1):#laço f no range de {n2} ate 1, diminuindo de -1
    n2 -= 1
    multi2 *= n2
    print(f'x{n2}', end='')
print(f' = {multi2}')
