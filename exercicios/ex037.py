num = int(input('Digite um número inteiro:'))
print('''Escolha uma dessas bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
escolha = int(input('Sua opção:'))
if escolha == 1:
    print(f'{num} convertido para binário é igual a {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} convertido para octal é igual  a {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}')
else:
    print('Opção INVALIDA! Escolha 1, 2 ou 3!')