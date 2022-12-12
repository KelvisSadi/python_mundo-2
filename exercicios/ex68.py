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
    #par impar
    if escolha == 'P' or escolha == 'I':
        if soma % 2 == 0:
            PouI = 'PAR'
        else:
            PouI = 'IMPAR'
        print(f'Você jogou {n}, o computador jogou {pc}. Total de {soma} deu {PouI}')
        if PouI == 'PAR' and escolha == 'P' or PouI == 'IMPAR' and escolha == 'I':
            print('\nGANHOU!\n'*3)
            print('-'*50)
            print('COMPUTADOR: Me de mais uma chance!')
        else:
            print(f'Perdeu! depois de {c} vitórias consecutivas')
            print('-'*50, '\nObrigado por Jogar. Volte sempre!' )
            break
        c += 1
    print('Opção invalida... Esolha [P] ou [I]')




