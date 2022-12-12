from random import randint
print('Par ou Impar')
c = n = 0
pc = randint(1, 30)
print('-'*50)
print('COMPUTADOR: Olá, tente me vencer no Par ou Impar!')
print('-'*50)
while True:
    print('COMPUTADOR: Pode escolher aí!')
    print('Escolha PAR ou IMPAR!')
    print('-'*50)
    escolha = str(input('Escolha [P] ou [I]:')).strip().upper()# variavel escolha par ou impar
    n = int(input('Agora digite o valor:'))# variavel escolha
    print('-'*50)
    soma = pc + n
    #se a escolha for P ou I faça
    if escolha == 'P' or escolha == 'I':
        if soma % 2 == 0:#Se o resto da divisão da {soma} por 2 for 0 faça
            PouI = 'PAR'
        else:            #se nao
            PouI = 'IMPAR'
        print(f'Você jogou {n}, o computador jogou {pc}. Total de {soma} deu {PouI}')
        if PouI == 'PAR' and escolha == 'P' or PouI == 'IMPAR' and escolha == 'I':#se escolheu par e a soma deu par ganhou, se escolheu impar e a soma deu impar ganhou
            print('\nGANHOU!\n'*3)
            print('-'*50)
            print('COMPUTADOR: Me de mais uma chance!')
        else:                                                                     #se não
            print(f'Perdeu! depois de {c} vitórias consecutivas')
            print('-'*50, '\nObrigado por Jogar. Volte sempre!' )
            break
        c += 1
    else:
        print('Opção invalida... Esolha [P] ou [I]')




