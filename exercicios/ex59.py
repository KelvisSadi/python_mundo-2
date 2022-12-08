print('Calculadora?')
n1 = float(input('Digite o primeiro valor:'))
n2 = float(input('Digite o segundo valor:'))
opçoes = 0
while opçoes != 5:#enquanto opçoes for diferente de 5 faça
    print('''
    [Escolha a operação]
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    
    [Outras escolhas]
    [ 4 ] escolher novos números
    [ 5 ] sair do programa
    ''')
    opçoes = int(input('Sua escolha:'))#opçoes recebe um inteiro
    if opçoes == 1:#se opçoes igual a 1 faça
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é igual a {soma:.2f}')
    elif opçoes == 2:#senao se opçoes igual a 2 faça
        mult = n1 * n2
        print(f'A multiplicação entre {n1} x {n2} é igual a {mult:.2f}')
    elif opçoes == 3:#senao se opçoes igual a 3 faça
        if n1 > n2:
            print(f'{n1} é o maior número')
        elif n2 > n1:
            print(f'{n2} é o maior número')
        else:
            print('Os valores são iguais')
    elif opçoes == 4:#senao se opçoes igual a 4 faça
        n1 = float(input('Digite um novo primeiro valor:'))
        n2 = float(input('Digite um novo segundo valor:'))
    elif opçoes == 5:
        print('Programa finalizado.')
    else:#senao se opçoes maior que 5 faça
        print('Opção invalida! Escolha umas dessas opções:[1][2][3][4][5]')



