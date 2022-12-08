from random import randint
quantidade_tentativas = 0
n_aleatorio = randint(1, 10)
acertou = False
print('Tente acertar o número mágico entre 1 e 10')
while not acertou:#enquanto acertou for falso
    chute = int(input('Seu chute:'))
    quantidade_tentativas += 1
    if chute < n_aleatorio:#se chute menor que n_aleatório faça
        print('Mais... Tente novamente!')
    elif chute > n_aleatorio:#se chute maior que n_aleatório faça
        print('Menos... Tente novamente!')
    else:#se nao faça
        acertou = True
print(f'Você acertou o número mágico [{n_aleatorio}] em {quantidade_tentativas} tentativas! Parabéns!!')