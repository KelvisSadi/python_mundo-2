from random import randint
print('Par ou Impar')
contador = jogador_num = 0
computador_num = randint(1, 30)
print('-'*50)
print('COMPUTADOR: Olá, tente me vencer no Par ou Impar!')
print('-'*50)
while True:  # while infinito n1
    print('COMPUTADOR: Pode escolher aí!')
    print('-' * 50)
    print('Escolha PAR ou IMPAR!')
    while True:  # while infinito n2
        escolha = str(input('Escolha [P] ou [I]:')).strip().upper()[0]  # variavel escolha par ou impar
        if escolha == 'P' or escolha == 'I':
            break  # break n2
    print('-' * 50)
    jogador_num = int(input('Agora digite o valor:'))  # variavel escolha
    print('-'*50)
    soma = computador_num + jogador_num
    # verificando Par ou Impar
    if soma % 2 == 0:  # se o resto da divisão da {soma} por 2 for 0 faça
        resultado = 'PAR'
    else:  # se nao
        resultado = 'IMPAR'
    # game
    print(f'Você jogou {jogador_num}, o computador jogou {computador_num}. Total de {soma} deu {resultado}')
    # game result
    if soma % 2 == 0 and escolha == 'P' or soma % 2 != 0 and escolha == 'I':  # se escolheu par e a soma deu par ganhou, se escolheu impar e a soma deu impar ganhou
        print('\nGANHOU!\n'*3)
        print('-'*50)
        print('COMPUTADOR: Me de mais uma chance!')
    else:  # se não
        print(f'Perdeu! depois de {contador} vitórias!')
        print('-'*50, '\nObrigado por Jogar. Volte sempre!')
        break  # break n1
    contador += 1
