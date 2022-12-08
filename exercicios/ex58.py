from random import randint
quantidade_tentativas = 0
n_aleatorio = randint(1, 11)
chute = 99
print('Tente acertar o número mágico entre 1 e 10')
while chute != n_aleatorio:
    chute = int(input('Seu chute:'))
    quantidade_tentativas += 1
print(f'Você acertou o número mágico que era {n_aleatorio} em {quantidade_tentativas} tentativas')