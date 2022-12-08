print('Programa que lê um inteiro e diz se ele é um númeor primo')
num = int(input('Digite um número:'))
if num % 2 == 0 or num % 3 == 0 or num == 1:#se o resto de num divido por 2 ou 3 for igual de 0 não é primo
    if num == 2 or num == 3:#se num for igual a 2 ou num for igual a 3 é primo
        print(f'{num} \033[1;97;40mÉ\033[m um número primo!')
    else:#senão
        print(f'{num} \033[1;97;40mNÃO\033[m é um número primo!')
else:#senão
    print(f'{num} \033[1;97;40mÉ\033[m um número primo!')

#jeito com for
print('lê um inteiro e diz se é primo com comando for')
num2 = int(input('Digite um inteiro:'))
total = 0
for analise in range(1, num2 + 1):#laço analise no range de 1 até num2
    if num2 % analise == 0:#se o resto da divisão de num2 por analise (que vai ser 1,2,3,4... até o num2 de novo) for igual zero faça
        total += 1#total recebe ele mesmo mais 1
if total == 2:#se total igual 2 faça. Lógica = número primo só é divisivel por 1 e ele mesmo ou seja 2 vezes, a variavel total recebe +1 cada vez que o numero foi dividido
    print(f'{num2} \033[1;97;40mÉ\033[m um número primo!')
else:
    print(f'{num2} \033[1;97;40mNÃO\033[m é um número primo!')
