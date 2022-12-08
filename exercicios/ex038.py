print('Verificador de números')
num_1 = float(input('Digite o primeiro valor:'))
num_2 = float(input('Digite o segundo valor:'))
if num_1 > num_2:
    print(f'O primeiro valor --> {num_1} é o maior!')
elif num_2 > num_1:
    print(f'O segundo valor --> {num_2} é o maior!')
else:
    print(f'Os valores digitados são equivalentes!')