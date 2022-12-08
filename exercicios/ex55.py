print('analisador  de peso menor e o maior')
menor = 0
maior = 0
#Lógica a primeira entrada vai ir para variavel maior e menor, pq tem 2 if's, ou seja é analisada toda vez pelas 2 indenpente, entao se a proxima for maior ou menor que a anterior irá substitui-la
for analise in range(1, 6):#laço analise no range de 5 vezes
    peso = float(input(f'Digite o peso [Kg] da {analise}ª pessoa:'))
    if analise == 1:#se o laço estiver na primeira vez faça. Lógica = na primeira leitura sempre irá salvar o peso como menor e maior e nas proximas vai comparando e substituindo se necessário
        menor = peso
        maior = peso
        posicao_menor = analise
        posicao_maior = analise
    else:
        if peso < menor:#se peso for menor que var menor faça
            menor = peso#menor recebe peso
            posicao_menor = analise
        if peso > maior:#se peso maior que var maior
            maior = peso#maior recebe peso
            posicao_maior = analise
print(f'A {posicao_maior}ª pessoa teve o maior peso de {maior} Kg\nA {posicao_menor}ª pessoa teve o menor peso de {menor} Kg')
