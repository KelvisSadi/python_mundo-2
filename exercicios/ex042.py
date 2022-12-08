print('Analisador de Triângulos')
r1 = float(input('Digite o valor da primeira reta:'))
r2 = float(input('Digite o valor da segunda reta:'))
r3 = float(input('Digite o valor da terceira reta:'))
#verifica se forma um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com estes valores é possivel formar um triângulo!')
    #verifica se todos os lados são iguais
    if r1 == r2 == r3:
        print('Com esses valores formou um triângulo equilátero: Todos os lados iguais!')
    #verifica se pelo menos 2 lados são iguais
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Com esses valores fomrou um triângulo isósceles: Dois lados iguais!')
    #nenhum lado igual
    else:
        print('Com esses valores formou um triângulo escaleno: Todos lados diferentes!')
else:
    print('Com esses valores NÃO É possível formar um triângulo!')